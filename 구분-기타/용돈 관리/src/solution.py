import sys

class Simulator:
    def __init__(self, N, out):
        self.N = N
        self.out = out
    
    def withdraw(self, K):
        self.count += 1
        self.money = K
        
    def buy(self):
        self.money -= self.out[self.day]
        self.day += 1
    
    def simulate(self, K):
        self.day = 0
        self.count = 0
        self.money = 0
        while self.day < self.N:
            if self.money < self.out[self.day]:
                self.withdraw(K)
            self.buy()
        
        return self.count

def binary_search(simulator: Simulator, M, start, end):
    
    while start <= end:
        mid = (start + end) // 2
        
        cnt = simulator.simulate(mid)
        
        if cnt > M:
            start = mid + 1
        
        else:
            answer = mid
            end = mid - 1
            
    return answer

def solution1():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    out = [0] * N
    for i in range(N):
        out[i] = int(input())

    min_k = max(out)
    max_k = sum(out)

    simulator = Simulator(N, out)
    answer = binary_search(simulator, M, min_k, max_k)

    print(answer)

class Solution:
    solution1 = staticmethod(solution1)

if __name__=='__main__':
    Solution.solution1()