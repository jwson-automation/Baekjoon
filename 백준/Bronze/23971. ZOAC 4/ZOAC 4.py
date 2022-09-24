y, x, a, b = map(int,input().split())

count = 0

for _ in range (0, y, a+1):
    for _ in range (0, x ,b+1):
        count += 1

print(count)