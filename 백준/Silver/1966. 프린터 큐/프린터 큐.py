import sys
from collections import deque


tc = int(input())
# 케이스만큼 반복
for _ in range (tc):
    # 문서갯수, 몇번째를 출력할지
    n, m = map(int,input().split())
    priority = list(map(int,input().split()))
    q = deque()
    count = 0

    for i in range(n):
        q.append((priority[i], i))

    
    priority.sort()
    while q:
        if max(priority) == q[0][0]:
            k = q.popleft()
            priority.remove(max(priority))
            count += 1
            if k[1] == m :
                print(count)
        else : 
            k = q.popleft()
            q.append(k)