import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    answer = 0
    while N >= 0:
        if N % 5 == 0:
            answer += N // 5
            print(answer)
            break
        N -= 3
        answer += 1
    else:
        print(-1)