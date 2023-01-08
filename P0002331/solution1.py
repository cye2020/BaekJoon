import sys


A, P = map(int, sys.stdin.readline().split())


def calculate(n):
    ret = 0
    for c in str(n):
        ret += int(c)**P
    return ret


if __name__ == '__main__':
    D = {A}
    l = 1
    c = {A: l}
    while True:
        next = calculate(A)
        D.add(next)
        l += 1
        A = next
        if len(D) != l:
            break
        c[A] = l
    print(c[A] - 1)