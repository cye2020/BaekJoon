import sys

def two_sum(nums, i):
    sumdict = {}
    n = nums[i]
    for j in range(len(nums)):
        if j == i: continue
        x = nums[j]
        if x in sumdict:
            return 1
        else: 
            sumdict[n-x] = x
    return 0    

def solution():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    
    answer = 0
    for i in range(N): answer += two_sum(nums, i)
    print(answer)


def solution1():
    input = sys.stdin.readline
    N = int(input())
    nums = list(map(int, input().split()))
    
    answer = 0
    for i in range(N): answer += two_sum(nums, i)
    print(answer)

def solution2():
    input = sys.stdin.readline
    N = int(input())
    nums = sorted(map(int, input().split()))
    
    answer = 0

    for k in range(N):
        find = nums[k]
        i = 0
        j = N-1
        while i < j:
            if i == k:
                i += 1
                continue
            if j == k:
                j -= 1
                continue
            if nums[i] + nums[j] == find:
                answer += 1
                break
            elif nums[i] + nums[j] < find:
                i += 1
            else:
                j -= 1
    print(answer)

if __name__=='__main__':
    solution()