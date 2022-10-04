from itertools import combinations

n, s = map(int,input().split())

numbers = list(map(int,input().split()))

count = 0

for a in range(1, n+1):
    tmp = combinations(numbers, a)
    for b in tmp:
        if sum(b) == s:
            count += 1

print(count)
