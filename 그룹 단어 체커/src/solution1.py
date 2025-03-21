import sys


def solution(N, words):
    count = N
    for word in words:
        char_list = [x for x in word]
        unique_char = list(set(char_list))
        
        for char in unique_char:
            num = char_list.count(char)
            first_index = char_list.index(char)
            last_index = len(char_list) - list(reversed(char_list)).index(char) - 1
            if last_index - first_index + 1 != num:
                count -= 1
                break
    return count
    

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    words = [sys.stdin.readline().strip() for _ in range(N)]
    
    answer = solution(N, words)
    print(answer)