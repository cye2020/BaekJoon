import sys

def solution(N, PS):
    for ps in PS:
        stack = []
        for p in ps:
            if p == "(":
                stack.append(p)
            else:
                if stack:
                    stack.pop()
                else:
                    print('NO')
                    break
        else:
            if stack:
                print('NO')
            else:
                print('YES')

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    PS = [sys.stdin.readline().strip() for _ in range(N)]
    solution(N, PS)