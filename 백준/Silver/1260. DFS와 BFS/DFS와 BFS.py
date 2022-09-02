import sys
from collections import deque

input = sys.stdin.readline

dot,lines,startdot = map(int,input().split())

graph = [[] for _ in range (0, dot+1)]

for i in range (lines):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    for i in graph[start]:
        if not visited[i]:
            dfs (graph, i, visited)

visited = [False]*(dot+1)

dfs (graph, startdot, visited)
print()

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    while queue:
        bubble = queue.popleft()
        print(bubble,end=' ')
        for i in graph[bubble]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

visited = [False]*(dot+1)

bfs (graph, startdot, visited)