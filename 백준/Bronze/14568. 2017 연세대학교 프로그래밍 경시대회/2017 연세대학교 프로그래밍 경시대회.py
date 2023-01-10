n = int(input())

cnt = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i + j + k != n:
                continue
            if k < j + 2:
                continue
            if i % 2 == 1:
                continue
            cnt += 1

print(cnt)
