import sys

class Game:
    def __init__(self, N, M, matrix):
        self.N = N
        self.M = M
        self.matrix = matrix
    
    def game_set(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.matrix[i][j] == 'R':
                    self.R = (i, j)
                elif self.matrix[i][j] == 'B':
                    self.B = (i, j)
                elif self.matrix[i][j] == 'O':
                    self.O = (i, j)
    
    def move(self, direction):
        if direction == 'U':
            if self.B[0] < self.A[0]:
                y, x = self.B
                while movable(self, y-1, x) == 1:
                    y -= 1
                pass
        elif direction == 'D':
            if self.B[0] > self.A[0]:
                # B가 먼저 움직임임
                pass
            pass
        elif direction == 'L':
            if self.B[1] < self.A[1]:
                # B가 먼저 움직임임
                pass
            pass
        elif direction == 'R':
            if self.B[1] > self.A[1]:
                # B가 먼저 움직임임
                pass
            pass

def movable(self, y, x):
    if self.matrix[y][x] == ".":
        return 1
    elif self.matrix[y][x] == "O":
        return 0
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, sys.stdin.readline().split())
    matrix = [list(map(str, sys.stdin.readline().strip('\n'))) for _ in range(N)]
    print(N, M)
    print(matrix)
    game = Game(N, M, matrix)
    game.game_set()
    print(game.R, game.B, game.O)
