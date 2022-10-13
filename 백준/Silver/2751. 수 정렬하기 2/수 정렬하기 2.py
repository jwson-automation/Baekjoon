from collections import deque

n = int(input())
q = []
for _ in range(n):
    q.append(int(input()))

q.sort()
q = deque(q)
while q:
    k = q.popleft()
    print(k)