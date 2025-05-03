import sys
from collections import deque
import copy

# L, U, R, D
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
class Marble:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def move(self, x, y):
        self.x = x
        self.y = y

class Game:
    def __init__(self, N, M, matrix):
        self.N = N
        self.M = M
        self.matrix = matrix
    
    def find_all(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.matrix[i][j] == 'R':
                    self.R = Marble(i, j, 'R')
                elif self.matrix[i][j] == 'B':
                    self.B = Marble(i, j, 'B')
                elif self.matrix[i][j] == 'O':
                    self.O = Marble(i, j, 'O')
    
    def move(self, r):
        _dx = dx[r]
        _dy = dy[r]
        
        # R, B의 위치를 비교하여 먼저 움직일 구슬을 정함
        if self.R.x * _dx + self.R.y * _dy < self.B.x * _dx + self.B.y * _dy:
            first_marble, second_marble = self.B, self.R
        else:
            first_marble, second_marble = self.R, self.B
        
        # 첫 번째 구슬이 이동
        while self.movable(first_marble.x + _dx, first_marble.y + _dy) == 1:
            self.matrix[first_marble.x + _dx][first_marble.y + _dy] = first_marble.color
            self.matrix[first_marble.x][first_marble.y] = '.'
            first_marble.move(first_marble.x + _dx, first_marble.y + _dy)
        
        # 만약 첫 번째 구슬이 구멍에 도착하면
        if self.movable(first_marble.x + _dx, first_marble.y + _dy) == 0:
            self.matrix[first_marble.x][first_marble.y] = '.'
            first_marble.move(first_marble.x + _dx, first_marble.y + _dy)
    
            
        # 두 번째 구슬이 이동
        while self.movable(second_marble.x + _dx, second_marble.y + _dy) == 1:
            self.matrix[second_marble.x + _dx][second_marble.y + _dy] = second_marble.color
            self.matrix[second_marble.x][second_marble.y] = '.'
            second_marble.move(second_marble.x + _dx, second_marble.y + _dy)
        
        # 만약 두 번째 구슬이 구멍에 도착하면
        if self.movable(second_marble.x + _dx, second_marble.y + _dy) == 0:
            self.matrix[second_marble.x][second_marble.y] = '.'
            second_marble.move(second_marble.x + _dx, second_marble.y + _dy)


    def movable(self, x, y):
        if x < 0 or x >= self.N or y < 0 or y >= self.M:
            return -1
        elif self.matrix[x][y] == ".":
            return 1
        elif self.matrix[x][y] == "O":
            return 0


def bfs(game: Game, k: int):
    q = deque()
    visited = [[[[False] * game.M for _ in range(game.N)] for _ in range(game.M)] for _ in range(game.N)]
    q.append([game, k])
    while q and (k < 10):
        g, k= q.popleft()
        # print(k, g.matrix)
        cur_game: Game = copy.deepcopy(g)
        for i in range(4):
            # 구슬의 왔다갔다 반복 방지
            new_game = copy.deepcopy(cur_game)
            new_game.move(i)
            if (visited[new_game.R.x][new_game.R.y][new_game.B.x][new_game.B.y]):
                continue
            visited[new_game.R.x][new_game.R.y][new_game.B.x][new_game.B.y] = True
            if new_game.B.x == new_game.O.x and new_game.B.y == new_game.O.y:
                    continue
            if new_game.R.x == new_game.O.x and new_game.R.y == new_game.O.y:
                return k + 1
            else:
                q.append([new_game, k + 1])
        del cur_game
    else:
        return -1


def solution(N, M, matrix):
    game = Game(N, M, matrix)
    game.find_all()
    return bfs(game, 0)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())
    matrix = [list(map(str, input().strip('\n'))) for _ in range(N)]
    answer = solution(N, M, matrix)
    print(answer)
