import sys

def solution1():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    
    obj = []
    DP = [0] * (K+1)
    
    for _ in range(N):
        W, V = map(int, input().split())
        obj.append((W, V))
    
    for w, v in obj:
        for i in range(K, w-1, -1):
            DP[i] = max(DP[i], DP[i-w] + v)
    answer = DP[K]
    print(answer)

class Solution:
    solution1 = staticmethod(solution1)

if __name__=='__main__':
    Solution.solution1()