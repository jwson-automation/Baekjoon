from collections import deque
import sys

input = sys.stdin.readline

F,S,G,U,D = map(int,input().split())
# floar, start, goal, up, down

graph = [0 for i in range(2000000)]

def inRange(number):
    return 0 < number <= F + 1

def bfs(start):
    queue = deque()
    queue.append(start)
    graph[start] = 1
    while queue:
        k = queue.popleft()
        for i in (U,-D):
            temp_k = k + i
            if inRange(temp_k):
                if graph[temp_k] == 0:
                    graph[temp_k] = graph[k]+1
                    queue.append(temp_k)


bfs(S)
if S ==G:
    print(0)
else:
    if graph[G] != 0:
            print(graph[G]-1)
    else:
        print('use the stairs')
        
    