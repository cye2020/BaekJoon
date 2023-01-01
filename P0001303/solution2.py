import sys
from typing import List


direction = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1],  # left
]


def dfs(graph: List[List[str]], v: int, visited: list(), search: list = list()):
    '''
    Depth-First Search
    
    v: int
        current vertex
    visited: List(bool)
        whether each vertex is visited or not
    search: list
        DFS result
    '''
    if not visited[v-1]:  # if not visited, visit.
        visited[v-1] = True
        search.append(v)
    for candidate in graph.adj[v]:  # visit adjacent vertexs
        if not visited[candidate-1]:  # not visited adjacent vertexs
            search = dfs(graph, candidate, visited, search)
    return search


if __name__ == '__main__':
    '''
    n: int
        width
    m: int
        height
    '''
    n, m = map(int, sys.stdin.readline().split())
    matrix = [list(map(str, sys.stdin.readline().strip('\n'))) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    print(matrix)
    print(visited)