import sys


n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(str, sys.stdin.readline().strip('\n'))) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
direction = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
]

def dfs(row: int, col: int, num: int):

    if not visited[row][col]:
        visited[row][col] = True
        num += 1
    
    color = matrix[row][col]

    for dir in direction:
        next_row = row + dir[0]
        next_col = col + dir[1]
        if (0 <= next_row < m) & (0 <= next_col < n):
            adj = matrix[next_row][next_col]
            if (not visited[next_row][next_col]) & (adj == color):
                num = dfs(next_row, next_col, num)
    return num

if __name__ == '__main__':
    '''
    n: int
        width of battlefield
    m: int
        height of battlefield
    '''
    power = {'W': 0, 'B': 0}
    for row in range(m):
        for col in range(n):
            if not visited[row][col]:
                num = dfs(row, col, 0)
                power[matrix[row][col]] += num**2
                
    print(power['W'], power['B'])