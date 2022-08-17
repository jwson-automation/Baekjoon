import sys

N, K = map(int,input().split())
Ai = []

for i in range(0, N):
        Ai.append(int(sys.stdin.readline()))
        Ai.sort(reverse=True)

count = 0
i = 0
for i in range(0, N):
    count += K//int(Ai[i])
    K = K%int(Ai[i])

print(count)