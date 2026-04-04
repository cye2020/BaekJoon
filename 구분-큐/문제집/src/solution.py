import sys

def solution1():
    import heapq
    input = sys.stdin.readline
    N, M = map(int, input().split())
    parent = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    queue = []
    
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        parent[B] += 1
    
    for i in range(N):
        if not parent[i+1]:
            heapq.heappush(queue, i+1)
    
    problems = []
    while queue:
        num = heapq.heappop(queue)
        problems.append(num)
        for ch in graph[num]:
            parent[ch] -= 1
            if not parent[ch]:
                heapq.heappush(queue, ch)
    
    print(*problems)
    

def solution2():
    from queue import PriorityQueue
    from collections import defaultdict
    
    input = sys.stdin.readline
    N, M = map(int, input().split())
    parent = defaultdict(int)
    child = defaultdict(list)
    queue = PriorityQueue(N+1)
    
    for _ in range(M):
        A, B = map(int, input().split())
        child[A].append(B)
        parent[B] += 1
    
    for i in range(N):
        if i+1 not in parent:
            queue.put(i+1)
    
    problems = []
    while not queue.empty():
        num = queue.get()
        problems.append(num)
        for ch in child[num]:
            parent[ch] -= 1
            if not parent[ch]:
                queue.put(ch)
    
    print(*problems)

class Solution:
    solution1 = staticmethod(solution1)
    solution2 = staticmethod(solution2)

if __name__=='__main__':
    Solution.solution1()