graph = list(map(int,input().split()))

for i in range(1, 1000001):
    tmp = 0
    for j in range(5):
        if i % graph[j] ==0:
            tmp += 1

    if tmp >= 3:
        print(i)
        break
