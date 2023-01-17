# 메모리 초과

import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
pyramid = list()


for i in range(n):
    pyramid.append(list(map(int, input().split())))
        

def bfs():
    queue = deque()
    queue.append([0, 0, pyramid[0][0]])  # 좌표, 합
    maxsum = 0
    while queue:
        floor, loc, sum = queue.popleft()
        if floor == n-1:
            maxsum = max(maxsum, sum)
        else:
            queue.append([floor + 1, loc, sum + pyramid[floor + 1][loc]])
            queue.append([floor + 1, loc + 1, sum + pyramid[floor+1][loc+1]])
    return maxsum


print(bfs())