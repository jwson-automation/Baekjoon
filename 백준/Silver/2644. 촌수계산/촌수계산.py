import sys
from collections import deque
input = sys.stdin.readline

def bfs(number):
    queue = deque()
    queue.append(number)
    while queue:
        k = queue.popleft()
        for i in graph[k]:
            if visited[i] == -1:
                visited[i] = visited[k] + 1
                queue.append(i)

n = int(input())

graph = [[] for i in range(n+1)]
visited = [-1 for i in range(n+1)]

start, end = map(int, input().split())

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[start] = 0
bfs(start)
print(visited[end])
