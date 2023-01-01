import sys


class One:
    def __init__(self, n) -> None:
        self.record = [n]
        self.op = [self.Divide(3), self.Divide(2), self.Minus(1)]
        self.current = 0
        self.stop = n
    
    class Divide:
        def __init__(self, n) -> None:
            self.num = n
        def __call__(self, n):
            if n % self.num == 0:
                return int(n / self.num)
            else:
                return 0
    
    class Minus:
        def __init__(self, n) -> None:
            self.num = n
        def __call__(self, n):
            return n - self.num
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == 0:
            self.current += 1
            self.record.append(0)
            return 0
        elif self.current < self.stop:
            candidate = [self.record[op(self.current+1)] for op in self.op]
            r = min(candidate) + 1
            self.current += 1
            self.record.append(r)
            return r
        else:
            raise StopIteration


                
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    one = One(n)
    for i in one:
        pass
    print(i)