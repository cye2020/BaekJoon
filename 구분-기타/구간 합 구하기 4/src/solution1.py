import sys

def solution():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    
    DP = [0] * (N + 1)
    for i in range(N):
        DP[i+1] = DP[i] + nums[i]
    
    for i in range(M):
        s, e = map(int, input().split())
        print(DP[e] - DP[s-1])
    
if __name__=='__main__':
    solution()