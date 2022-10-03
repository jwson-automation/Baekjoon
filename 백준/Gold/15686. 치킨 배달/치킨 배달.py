from itertools import combinations
import sys

n,m = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range (n)]

chicken = []
house = []

answer = sys.maxsize

for a in range(n):
    for b in range(n):
        if graph[a][b] == 1:
            house.append((a,b))
        if graph[a][b] == 2:
            chicken.append((a,b))
            
for i in combinations(chicken, m):
    tmp = 0
    for hy, hx in house :
        distance = sys.maxsize
        for cy, cx in i:
            distance = min(distance, abs(cx - hx) + abs(cy - hy))
        tmp += distance
    answer = min(answer, tmp)
print(answer)

