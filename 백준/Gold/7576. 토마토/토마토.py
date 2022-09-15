import sys
from collections import deque

# 시간 아껴주기
input = sys.stdin.readline

# 입력값
x, y = map(int,input().split())

# 2차원으로 넣어주기
graph = [list(map(int, input().split())) for _ in range(y)]

# 그래프에서 토마토 위치 Queue에 넣기
queue = deque()
for b in range(y):
    for c in range(x):
        if graph[b][c] == 1:
            queue.append((b,c,0))

# 방향
dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 범위 조절
def inRange(y1, x1):
    return 0 <= x1 < x and 0 <= y1 < y
# 1 자리를 넣은 걸
while queue:
    y2,x2,answer = queue.popleft()
    for i in range(4):
        ny = y2 + dy[i]
        nx = x2 + dx[i]
        nanswer = answer + 1
        if inRange(ny,nx):
            if graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append((ny,nx,nanswer))

# # 토마토 남아있으면 -1 꺼내기 

for b in range(y):
    if graph[b].count(0) > 0:
        answer = -1
        break

print(answer)

