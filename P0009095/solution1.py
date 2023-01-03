import sys


def factorial(r):
    ret = 1
    for i in range(r):
        ret *= (i+1)
    return ret


def combination(n, r):
    ret = 1
    for i in range(r):
        ret *= (n-i)
    ret //= factorial(r)
    return ret


def partition(count):
    s = sum(count)
    ret = 1
    for n in count:
        ret *= combination(s, n)
        s -= n
    return ret


def calculate(sum, nums, count, n):
    now = nums[n:]
    
    if n == len(nums) - 1:
        count[n] = sum // nums[n]
        return partition(count)
    
    ret = 0
    for i in range(sum // now[0] + 1):
        count[n] = i
        ret += calculate(sum - i * now[0], nums, count, n+1)
    return ret


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = [3, 2, 1]
    count = [-1, -1, -1]
    testcase = list(int(sys.stdin.readline()) for _ in range(n))
    for i in range(n):
        print(calculate(testcase[i], nums, count, 0))
    
    