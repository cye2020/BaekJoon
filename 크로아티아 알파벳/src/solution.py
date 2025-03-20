import sys

alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

def solution1(alphabet):
    count = 0
    while len(alphabet) > 1:
        for i in alpha_list:
            if alphabet.startswith(i):
                alphabet = alphabet[len(i):]
                break
        else:
            alphabet = alphabet[1:]
        count += 1
    if len(alphabet) == 1:
        count += 1
    return count

def solution2(alphabet):
    for i in alpha_list:
        alphabet = alphabet.replace(i, " ")
    return len(alphabet)


if __name__ == "__main__":
    alphabet = sys.stdin.readline().strip()
    count = solution(alphabet)
    print(count)