import sys
import copy
from collections import deque

input = sys.stdin.readline

Y, X = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(Y)]
graph2 = copy.deepcopy(graph)


visited = [[0 for _ in range(X)]for _ in range(Y)]

bingsan = 0
year = 0

dy = [0, 0 ,-1, 1]
dx = [-1, 1, 0, 0]

def inRange(y, x):
    return 0 <= y < Y and 0 <= x < X


def counting(y,x):
    visited[y][x] = 1
    q = deque()
    q.append((y,x))
    while q:
        y1, x1 = q.popleft()
        for i in range(4):
            y2 = y1 + dy[i]
            x2 = x1 + dx[i]
            if inRange(y2,x2) and graph[y2][x2] != 0 and visited[y2][x2] != 1:
                    q.append((y2,x2))
                    visited[y2][x2] = 1


def melt(y,x):
        for i in range(4):
            if graph2[y][x] > 0:
                y2 = y + dy[i]
                x2 = x + dx[i]
                if inRange(y2,x2):
                    if graph[y2][x2] == 0:
                        graph2[y][x] -= 1

while bingsan < 2:
    bingsan =0
    maxValue = max(map(max, graph))
    if maxValue == 0:
        year = 0
        break
    else:
        for a in range(Y):
            for b in range(X):
                if graph[a][b] != 0 and visited[a][b] == 0:
                    counting(a,b)
                    bingsan += 1
                    # print(bingsan)
        if bingsan < 2:
            year += 1
        # print('melt')

        for a in range(Y):
            for b in range(X):
                if graph[a][b] != 0:
                    melt(a,b)
                
        visited = [[0 for _ in range(X)]for _ in range(Y)]
        graph = copy.deepcopy(graph2)
    


# print('2',graph)

# print('bingsan',bingsan)

print(year)