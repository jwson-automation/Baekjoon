import sys
import heapq

input = sys.stdin.readline

# 정점갯수, 간선갯수
v, e = map(int, input().split())
# 시작점
start = int(input())

# u 에서 b 로 가는데 가중치가 w 인 간선
INF = sys.maxsize
graph = [ [] for _ in range(v+1)]
visited = [ 0 for _ in range(v+1)]
count = [ INF for _ in range(v+1)]
tmp = []

#2차원 그래프에 담기
for i in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

# BFS로 돌리기
heap = []
heapq.heappush(heap,(0,start))
count[start] = 0

while heap:
    min_count, node = heapq.heappop(heap)

    if visited[node] == 1:
        continue
    
    visited[node] = 1
    # 연결된 값 찾아서 node에 넣어주기

    for num, plus in graph[node]:
        new_count = min_count + plus

        if new_count < count[num]:
            count[num] = new_count
            heapq.heappush(heap,(count[num],num))
    

for answer in range(1, v+1):
    if count[answer] == INF:
        print('INF')
    else:
        print(count[answer])

# 인접 행렬 > 인접 리스트
# 레퍼런스 : https://www.acmicpc.net/board/view/34516