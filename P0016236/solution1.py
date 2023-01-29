import sys
from collections import deque


input = sys.stdin.readline
N = int(input())

baby = None
fishes = 0
space = None
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def isFish(s, i, j):
    global baby, fishes
    s = int(s)
    if s == 0:
        return None
    elif s == 9:
        baby = BabyShark(i, j)
        return baby
    else:
        global fishes
        fishes += 1
        fish = Fish(s, i, j)
        return fish


class Fish:
    def __init__(self, size, y, x, dist=0):
        self.size = size
        self.loc = (y, x)
        self.dist = dist


class BabyShark(Fish):
    def __init__(self, y, x):
        super().__init__(2, y, x)
        self.exp = 0
        self.time = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        global space, fishes, N
        visited = [[False] * N for _ in range(N)]
        queue = deque()
        queue.append([*self.loc, 0, 0])
        target = Fish(0, N, N, N*N)
        
        # print(f'------Fishes: {fishes}-----------')
        if fishes == 0:
            raise StopIteration

        while queue:
            y, x, dist, exp = queue.popleft()
            if dist + 1 > target.dist:
                break
            # print(f'Current: {y}, {x}, size: {self.size}')
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (ny < 0) or (nx < 0) or (ny >= N) or (nx >= N) or (visited[ny][nx]):
                    continue
                visited[ny][nx] = True
                if space[ny][nx] is not None:
                    fish = space[ny][nx]
                    if fish.size < self.size:
                        # print(f'Candidate: {(ny, nx, dist + 1)}')
                        if fish.loc < target.loc:
                            fish.dist = dist + 1
                            target = fish
                    elif fish.size == self.size:
                        queue.append([ny, nx, dist + 1, exp + 1])
                else:
                    # print(f'Append: {ny} {nx}')
                    queue.append([ny, nx, dist + 1, exp + 1])
        
        if target.size > 0:
            self.move(*target.loc, target.dist)
            # print(f'Eat {target.loc}')
        else:
            raise StopIteration


    def eat(self, fish):
        global space, fishes
        space[fish.loc[0]][fish.loc[1]] = None
        fishes -= 1
        
        self.exp += 1
        if self.exp == self.size:
            self.levelUp()
    
    def levelUp(self):
        self.exp = 0
        self.size += 1

    def move(self, i, j, dist):
        global space
        space[self.loc[0]][self.loc[1]] = None
        self.eat(space[i][j])
        self.time += dist
        self.loc = (i, j)
        space[i][j] = self
        

if __name__ == '__main__':
    space = [[isFish(s, i, j) for j, s in enumerate(input().split())] for i in range(N)]
    for i in baby:
        pass
    
    print(baby.time)