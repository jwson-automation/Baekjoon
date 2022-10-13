n = int(input())
numbers = []
for _ in range(n):
    a, b = map(int,input().split())
    numbers.append((a,b))
numbers.sort()

for k in numbers:
    print(k[0],k[1])
