from itertools import count
from operator import truediv


T = int(input())
graph = []

for _ in range(T):
    graph.append(list(map(int, input())))

visited = [[True for _ in range(T)] for _ in range (T)]

vector_X = [ 0, 1, -1, 0]
vector_Y = [ 1, 0, 0, -1]
    
def inRange(y, x):
    global T
    return 0<=y<T and 0<=x<T

def dfs(y, x):
    global score
    visited[y][x] = False
    for d in range(4):
        x1 = x + vector_X[d]
        y1 = y + vector_Y[d]
        if inRange(y1, x1):
            if graph[y1][x1] == 1:
                if visited[y1][x1]:
                    score += 1
                    dfs(y1, x1)

count = 0
answer = []

for i in range(T):
    for k in range(T):
        if visited[i][k]:
            if graph[i][k] == 1:
                score = 1
                count += 1
                dfs(i,k)
                answer.append(score)
                answer.sort()

print(count)
for i in answer:
    print(i)
                

