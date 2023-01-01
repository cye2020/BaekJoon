import sys
from typing import List

class Country:
    def __init__(self, color: str) -> None:
        self.color = color
        self.power = 0


class Soldier:
    def __init__(self, color: str) -> None:
        self.color = color
        self.visited = False


class Battlefield:
    def __init__(self, w: int, h: int, field: List[List[Soldier]]) -> None:
        self.width = w
        self.height = h
        self.field = field
        self.visited = [[False] * n for _ in range(m)]
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
    
    def possible(self, row, col):
        updown = 0 <= row < self.height
        leftright = 0 <= col < self.width
        return updown & leftright


def dfs(battlefield: Battlefield, row: int, col: int, num: int):
    soldier = battlefield.field[row][col]

    # if not soldier.visited:
    #     soldier.visited = True
    #     num += 1
    if not battlefield.visited[row][col]:
        battlefield.visited[row][col] = True
        num += 1

    for dir in battlefield.direction:
        next_row = row + dir[0]
        next_col = col + dir[1]
        if battlefield.possible(next_row, next_col):
            adj = battlefield.field[next_row][next_col]
            # if (not adj.visited) & (adj.color == soldier.color):
            if (not battlefield.visited[next_row][next_col]) & (adj.color == soldier.color):
                num = dfs(battlefield, next_row, next_col, num)
    return num

if __name__ == '__main__':
    '''
    n: int
        width of battlefield
    m: int
        height of battlefield
    '''
    n, m = map(int, sys.stdin.readline().split())
    matrix = [list(map(Soldier, sys.stdin.readline().strip('\n'))) for _ in range(m)]
    battlefield = Battlefield(n, m, matrix)
    battlefield.enter(['B', 'W'])
    for row in range(m):
        for col in range(n):
            soldier = battlefield.field[row][col]
            if not battlefield.visited[row][col]:
                num = dfs(battlefield, row, col, 0)
                battlefield.countries[soldier.color].power += num**2

    our: Country = battlefield.countries['W']
    enemy: Country = battlefield.countries['B']
    print(our.power, enemy.power)