from collections import deque

n,k = map(int,input().split())

answer = []
q = deque()

for a in range(1,n+1):
    q.append(a)

count = 1
while q:
    if count == k:
        tmp = q.popleft()
        answer.append(tmp)
        count = 1
    else :
        move = q.popleft()
        q.append(move)
        count += 1
   
   
a = ", ".join(map(str, answer))
print('<',a,'>',sep="")

