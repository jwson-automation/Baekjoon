import heapq

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
answer = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
# print(visited)


heap = []
heapq.heappush(heap, 1)
while heap:
    k = heapq.heappop(heap)
    for i in graph[k]:
        if visited[i] == 0:
            visited[i] = 1
            answer[i] = k
            heapq.heappush(heap,i)

for tmp in range(2,n+1):
    print(answer[tmp])


