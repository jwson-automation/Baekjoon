computer = int(input())
line = int(input())
count = []

graph = [[]for i in range (0, computer+1)]
visited = [False for i in range (0, computer+1)]
for i in range(line):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# print(graph)
# print(visited)


def dfs(graph, start, visited):
    visited[start] = True
    count.append(start)
    for i in (graph[start]):
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)

print(len(count)-1)