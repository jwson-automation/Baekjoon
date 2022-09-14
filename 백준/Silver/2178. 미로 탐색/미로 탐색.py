import sys
from collections import deque

input = sys.stdin.readline

def dfs(number):
    queue = deque()
    queue.append(number)
    while queue:
        k = queue.popleft()
        for i in connection[k]:
            if visited[i] == 0:
                visited[i] = visited[k]+1
                queue.append(i)

y, x = map(int,input().split())

graph = []

visited = [0for i in range(x*y)]

for _ in range(y):
    temp = list(map(int, input().rstrip()))
    graph.append(temp)

connection = [[] for _ in range((x*y))]

start = 0
while start != (x*y-1):
    y1 = start//x
    x1 = start%x
    if x > x1+1 > -1:
        if graph[y1][x1+1] == 1:
            connection[start].append(start+1)
    if x > x1-1 > -1:
        if graph[y1][x1-1] == 1:
            connection[start].append(start-1)
    if y > y1+1 > -1:
        if graph[y1+1][x1] == 1:
            connection[start].append(start+x)
    if y > y1-1 > -1:
        if graph[y1-1][x1] == 1:
            connection[start].append(start-x)
    start += 1

dfs(0)

print(visited[(x*y -1)]+1)