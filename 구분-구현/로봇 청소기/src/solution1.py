from sys import stdin

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

class Machine:
    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d
        self.work = 0
    
    def order(self, N, M, room):
        self.room = room
        self.N = N
        self.M = M
        
    def __iter__(self):
        return self
    
    def __next__(self):
        # print((self.r, self.c, self.room[self.r][self.c]), end=' ')
        if self.room[self.r][self.c] == 0:
            self.clean()
            return self.work
        for _ in range(4):
            self.d = self.rotate(-1)
            new_r = self.r + dx[self.d]
            new_c = self.c + dy[self.d]
            # print(new_r, new_c, self.d, end=' ')
            if (0 <= new_r < self.N) and (0 <= new_c < self.M):
                if self.room[new_r][new_c] == 0:
                    self.r, self.c = (new_r, new_c)
                    self.clean()
                    return self.work
        else:
            d = self.rotate(2)
            new_r = self.r + dx[d]
            new_c = self.c + dy[d]
            if self.room[new_r][new_c] == 1:
                raise StopIteration
            else:
                self.r, self.c = (new_r, new_c)
                return self.work

    def rotate(self, R):
        return (self.d + R) % 4

    def clean(self):
        self.room[self.r][self.c] = -1
        self.work += 1

def solution(r, c, d, N, M, room):
    machine = Machine(r, c, d)
    machine.order(N, M, room)
    for work in machine:
        pass
    return work


if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    r, c, d = map(int, stdin.readline().split())
    room = [list(map(int, stdin.readline().split())) for _ in range(N)]
    answer = solution(r, c, d, N, M, room)
    print(answer)