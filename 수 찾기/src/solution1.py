import sys

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    A = sorted(list(map(int, sys.stdin.readline().split())))
    M = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))
    
    for i in B:
        print(binary_search(A, i))