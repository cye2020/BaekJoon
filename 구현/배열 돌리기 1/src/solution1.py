from sys import stdin

class Cell():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

class Layer(object):
    def __init__(self, layer, N, M):
        self.layer = layer
        self.cells = []
        x_min = layer
        x_max = N - layer - 1
        y_min = layer
        y_max = M - layer - 1
        self.cells.extend([(i, layer) for i in range(layer, x_max)])
        self.cells.extend([(x_max, j) for j in range(layer, y_max)])
        self.cells.extend([(i, y_max) for i in range(x_max, x_min, -1)])
        self.cells.extend([(x_min, j) for j in range(y_max, y_min, -1)])

    def rotate(self, R):
        new_cells = self.cells.copy()
        for i in range(len(self.cells)):
            new_cells[i] = self.cells[(i + R) % len(self.cells)]
        return new_cells


def solution(N, M, R, matrix):
    max_layer = min(N, M) // 2
    layers = [Layer(i, N, M) for i in range(max_layer)]
    new_matrix = [[0] * M for _ in range(N)]
    for layer in layers:
        new_cells = layer.rotate(R)
        for (i, j), (x, y) in zip(layer.cells, new_cells):
            new_matrix[x][y] = matrix[i][j]
    return new_matrix

if __name__ == '__main__':
    N, M, R = map(int, stdin.readline().split())
    matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]
    answer = solution(N, M, R, matrix)
    for row in answer:
        print(*row)