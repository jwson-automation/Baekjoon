from collections import deque

# 디에프에스 외운거 때려넣고
def bfs(number):
    queue = deque()
    queue.append(number)
    while queue:
        k = queue.popleft()
        # 도달하면 바로 출력, 멈춤으로 시간 아끼기
        if k == D:
            print(graph[k])
            break
        
        for i in (k-1,k+1,k*2):
            if 0<= i <= (100000) and not graph[i]:
                graph[i] = graph[k] + 1
                queue.append(i)
# 입력값 받기
S, D = map(int,input().split())

# 필요한 만큼의 그래프 만들기 1차원
graph = [0 for _ in range(100001)]


bfs(S)
