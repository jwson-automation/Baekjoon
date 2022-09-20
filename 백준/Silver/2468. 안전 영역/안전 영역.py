import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

graph = [list(map(int,input().split())) for _ in range(T)]
visited = [[0 for _ in range(T)]for _ in range(T)]
maxValue = max(map(max, graph))
water = 0
answer = 0

dy = [0, 0 ,-1, 1]
dx = [-1, 1, 0, 0]

def inRange(number1, number2):
    return 0 <= number1 < T and 0 <= number2 < T

q = deque()

def bfs(y,x):
    global water
    global answer
    visited[y][x] = 1
    q.append((y,x))
    while q:
        y1,x1 = q.popleft()
        for i in range(4):
            y2 = y1 + dy[i]
            x2 = x1 + dx[i]
            if inRange(y2,x2) and graph[y2][x2] > water and visited[y2][x2] == 0:
                visited[y2][x2] = 1
                q.append((y2,x2))
temp = []

while maxValue > water:
    visited = [[0 for _ in range(T)]for _ in range(T)]
    water += 1
    answer = 0
    # print(water)
    for a in range (T):
        for b in range (T):
            if visited[a][b] == 0 and graph[a][b] > water:
                bfs(a,b)
                answer += 1
                # print(answer)
    temp.append(answer)
if max(temp) == 0 :
    print(1)
else:
    print(max(temp))
