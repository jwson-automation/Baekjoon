from collections import deque


def bfs():
    global count
    for a in range (n):
        for b in range (n):
            if visited[a][b] == 0:
                visited[a][b] = 1
                count +=1
                q.append((a,b))
            while q:
                y, x = q.popleft()
                for i in range (4):
                    y2 = y + dy[i]
                    x2 = x + dx[i]
                    if 0<= y2 < n and 0<= x2 < n and visited[y2][x2] == 0:
                        if graph[y][x] == graph[y2][x2]:
                            visited[y2][x2] = 1
                            q.append((y2,x2))
                            

n = int(input())
graph = [list(map(str,input().rstrip())) for _ in range (n)]
visited = [[0]*n for _ in range (n)]


dy = [-1,1,0,0]
dx = [0,0,-1,1]

q = deque()
count = 0

bfs()
tmp = count
count = 0
visited = [[0]*n for _ in range (n)]
for a in range(n):
    for b in range(n):
        if graph[a][b] == 'R':
            graph[a][b] = 'G'

bfs()
print(tmp,count)