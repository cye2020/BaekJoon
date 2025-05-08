import sys
from collections import deque


class Cell:
    def __init__(self, num) -> None:
        self.num = int(num)
        self.visited = False
        self.distance = 1


class Maze:
    def __init__(self, n, m, matrix) -> None:
        self.height = n
        self.width = m
        self.matrix = matrix
        self.direction = [
            [-1, 0],  # up
            [0, 1],  # right
            [1, 0],  # down
            [0, -1],  # left
        ]

    def possible(self, row, col):  # 가능한 좌표인가
        updown = 0 <= row < self.height
        leftright = 0 <= col < self.width
        return updown & leftright
    
    def movable(self, row, col):
        return (self.matrix[row][col].num == 1)
    
    def end(self, row, col):
        return (row == self.height - 1) & (col == self.width - 1)


def bfs(maze, row, col):
    cell = maze.matrix[row][col]
    cell.visited = True
    
    queue = deque()
    queue.append((row, col))
    
    while queue:
        row, col = queue.popleft()
        cell = maze.matrix[row][col]

        if maze.end(row, col):
            break
        for dir in maze.direction:
            next_row = row + dir[0]
            next_col = col + dir[1]
            if maze.possible(next_row, next_col):
                if maze.movable(next_row, next_col):
                    adj = maze.matrix[next_row][next_col]
                    if (not adj.visited):
                        queue.append((next_row, next_col))
                        adj.visited = True
                        adj.distance = cell.distance + 1
    return cell.distance


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    matrix = [list(map(Cell, sys.stdin.readline().strip('\n'))) for _ in range(n)]
    
    maze = Maze(n, m, matrix)
    move = bfs(maze, 0, 0)
    print(move)