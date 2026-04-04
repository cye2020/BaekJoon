import sys

def solution1():
    input = sys.stdin.readline
    
    DP = [[[1] * 21 for _ in range(21)] for _ in range(21)]
    
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if i < j < k:
                    DP[i][j][k] = DP[i][j][k-1] + DP[i][j-1][k-1] - DP[i][j-1][k]
                else:
                    DP[i][j][k] = DP[i-1][j][k] + DP[i-1][j-1][k] + DP[i-1][j][k-1] - DP[i-1][j-1][k-1]
    
    while True:
        a, b, c = map(int, input().split())

        if (a == -1 and b == -1 and c == -1):
            break
        
        if min(a, b, c) <= 0:
            val = 1
        
        elif max(a, b, c) > 20:
            val = DP[20][20][20]
        
        else:
            val = DP[a][b][c]
        print(f'w({a}, {b}, {c}) = {val}')

class Solution:
    solution1 = staticmethod(solution1)

if __name__=='__main__':
    Solution.solution1()