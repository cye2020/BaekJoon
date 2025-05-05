from sys import stdin

def solution(K, values):
    answer = 0
    
    for i in range(len(values)-1, -1, -1):
        n = values[i]
        if n > K:
            continue
        q = K // n
        K = K % n
        answer += q
        if K <= 0:
            break
    return answer

if __name__ == '__main__':
    input = stdin.readline
    N, K = map(int, input().split())
    values = [int(input()) for _ in range(N)]
    
    answer = solution(K, values)
    print(answer)