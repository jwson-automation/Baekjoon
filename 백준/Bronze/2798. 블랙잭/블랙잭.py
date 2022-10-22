from itertools import combinations

n, m = map(int,input().split())

numbers = list(map(int,input().split()))
answer = []

for k in combinations (numbers, 3):
    if sum(k) <= m :
        answer.append(sum(k))

print(max(answer))