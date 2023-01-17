import sys
sys.setrecursionlimit(10**8)


input = sys.stdin.readline

S, T = input().strip(), input().strip()
length = len(T)

print(T.index(S))

# def process(s):
#     if s == T:
#         return 1
#     elif len(s) >= length:
#         return 0
#     return process(s + 'A') | process((s[::-1] + 'B'))
    
# print(process(S))