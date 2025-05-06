import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    r5 = N // 5
    q = N % 5
    if N == 4 or N == 7:
        print(-1)
    else:
        print(r5 + q//3 + q%3)