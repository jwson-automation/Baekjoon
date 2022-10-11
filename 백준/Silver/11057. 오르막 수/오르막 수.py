import sys

n = int(input())

graph = [[0 for _ in range(10)] for _ in range(n+2)]

if n == 0:
    print(0)
    sys.exit()
if n == 1:
    print(10)
    sys.exit()

for y in range(1, n+2):
    graph[y][0] = 1
    graph[y][1] = y
    for x in range(2, 10):
        if y == 1:
            graph[y][x] == 1
        graph[y][x] = graph[y-1][x] + graph[y][x-1]

# print(graph)

print(graph[n+1][9]%10007)
