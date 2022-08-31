from collections import deque
N = int(input())
queue = deque([i for i in range(1,N+1)])

if N == 1: print(1)

i = 0
while queue:
    i += 1
    if i%2 != 0:
        queue.popleft()
    elif len(queue) == 1:
        print(queue[0])    
    else:
        tmp = queue.popleft()
        queue.append(tmp)
    
