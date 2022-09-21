import sys
from collections import deque


input = sys.stdin.readline

Y, X = map(int,input().split())

sy, sx, di = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range (Y)]
visited = [[0 for _ in range (X)] for _ in range (Y)]

count = 0

# print(graph)

dx = [0 ,1, 0, -1]
dy = [-1, 0, 1, 0]

def inRange(y, x):
    return 0 <= y < Y and 0 <= x < X

def Wall(y,x):
    return graph[y][x] == 1


def counting():
    global count
    for a in range(Y):
        for b in range(X):
            if visited[a][b] == 1:
                count += 1
    print(count)

def bfs (y, x, d):
    q = deque()
    q.append((y,x,d))
    while q:
        y, x, d = q.popleft()
        visited[y][x] = 1
        tmp = d
        for i in range(4):
            tmp -= 1
            
            if tmp == -1: tmp = 3

            y2 = y + dy[tmp]
            x2 = x + dx[tmp]

            if inRange(y2,x2) and visited[y2][x2] == 0 and not Wall(y2,x2):
                visited[y2][x2] = 1
                q.append((y2,x2,tmp))
                break

            elif i == 3 and inRange(y2,x2):
                tmp =(d+2)%4
                y2 = y + dy[tmp]
                x2 = x + dx[tmp]
                if Wall(y2,x2):
                    counting()
                else : q.append((y2,x2,d))
                    

bfs(sy,sx,di)
# print(visited)





