'''
record all fibonacci number
'''

import sys


class Fibonacci:
    def __init__(self, n) -> None:
        self.fn = [0, 1]
        self.current = 0
        self.stop = n + 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == 0:
            self.current += 1 
            return 0
        elif self.current == 1:
            self.current += 1 
            return 1
        elif self.current < self.stop:
            r = self.fn[-1] + self.fn[-2]
            self.fn.append(r)
            self.current += 1 
            return r
        else:
            raise StopIteration

                
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    fibo = Fibonacci(n)
    for i in fibo:
        pass
    print(i)