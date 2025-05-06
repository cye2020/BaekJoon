from sys import stdin
from itertools import combinations


def solution(M, cards):
    answer = 0
    
    for i0, i1, i2 in combinations(range(len(cards)), 3):
        sum_cards = cards[i0] + cards[i1] + cards[i2]
        if sum_cards == M:
            return M
        if (sum_cards < M) and (sum_cards > answer):
            answer = sum_cards
    return answer

if __name__ == '__main__':
    input = stdin.readline
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    
    answer = solution(M, cards)
    print(answer)