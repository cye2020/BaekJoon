import sys
from typing import List


class Country:
    def __init__(self, color: str) -> None:
        self.color = color
        self.power = 0
        self.army: List[Force] = list()
    
    def reinforce(self):
        self.army.append(Force())
        
    def calculate_power(self):
        for force in self.army:
            self.power += force.num**2

    def show_army(self):
        for force in self.army:
            print(force.num)


class Force:
    def __init__(self) -> None:
        self.soldiers: List[Soldier] = list()
        self.num = 0
        
    def enter(self, soldier):
        self.soldiers.append(soldier)
        self.num += 1


class Soldier:
    def __init__(self, color: str) -> None:
        self.color = color
        self.visited = False


class Battlefield:
    def __init__(self, h: int, w: int, field: List[List[Soldier]]) -> None:
        self.width = w
        self.height = h
        self.field = field
        self.countries = dict()
        self.direction = [
            [-1, 0],  # up
            [0, 1],  # right
            [1, 0],  # down
            [0, -1],  # left
        ]
    
    def enter(self, colors: List[str]):
        for color in colors:
            country = Country(color)
            self.countries.update({color: country})
    
    def possible(self, p):
        '''
        p: tuple
            point to check if it is in field
        '''
        updown = (p[0] < self.height) & (p[0] >= 0)
        leftright = (p[1] < self.width) & (p[1] >= 0)
        return updown & leftright


def search(battlefield: Battlefield, row: int, col: int, num: int, enemy: set):
    soldier = battlefield.field[row][col]
    country: Country = battlefield.countries[soldier.color]
    
    if num == 0:
        country.reinforce()

    if not soldier.visited:
        soldier.visited = True
        country.army[-1].enter(soldier)
        num += 1

    for dir in battlefield.direction:
        next_row = row + dir[0]
        next_col = col + dir[1]
        if battlefield.possible((next_row, next_col)):
            adj = battlefield.field[next_row][next_col]
            if (adj.color == soldier.color) & (not adj.visited):
                search(battlefield, next_row, next_col, num, enemy)
            elif (adj.color != soldier.color) & (not adj.visited):
                enemy.add((next_row, next_col))
    
    if num > 1:
        return

    for e in enemy:
        adj = battlefield.field[e[0]][e[1]]
        if not adj.visited:
            search(battlefield, e[0], e[1], 0, set())


if __name__ == '__main__':
    '''
    n: int
        width of battlefield
    m: int
        height of battlefield
    '''
    m, n = map(int, sys.stdin.readline().split())
    matrix = []
    for row in range(n):
        matrix.append(list(map(Soldier, sys.stdin.readline().strip('\n'))))
    
    battlefield = Battlefield(n, m, matrix)
    battlefield.enter(['B', 'W'])
    search(battlefield, 0, 0, 0, set())
    our: Country = battlefield.countries['W']
    enemy: Country = battlefield.countries['B']
    
    our.calculate_power()
    enemy.calculate_power()
    print(our.power, enemy.power)