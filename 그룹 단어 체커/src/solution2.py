N = int(input())
count = 0

for _ in range(N):
    string = input()
    print(sorted(string, key=string.find))
    if list(string) == sorted(string, key=string.find):
        count += 1

print(count)



# 출처: https://www.acmicpc.net/source/84656511