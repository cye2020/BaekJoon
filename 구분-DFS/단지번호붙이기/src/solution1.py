from sys import stdin

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, N, matrix, visited):
    stack = [(x, y)]
    home = 0
    
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        
        visited[x][y] = True
        home += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 1 and not visited[nx][ny]:
                stack.append((nx, ny))
    return home


def solution(N, matrix):
    num = 0
    home_num = []
    visited = [[False] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 and not visited[i][j]:
                home = dfs(i, j, N, matrix, visited)
                num += 1
                home_num.append(home)
    answer = [num, *sorted(home_num)]
    return answer

if __name__ == '__main__':
    input = stdin.readline
    N = int(input())
    matrix = [list(map(int, list(input().strip()))) for _ in range(N)]
    
    answer = solution(N, matrix)
    for a in answer:
        print(a)
    
    