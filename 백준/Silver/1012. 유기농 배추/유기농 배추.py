import sys
sys.setrecursionlimit(10 ** 8 )

input = sys.stdin.readline

def dfs(x:int, y:int):
    if x<0 or x>=N or \
        y<0 or y >= M :
        return False # 경계값을 넘기지 못하도록 조건문

    if graph[x][y] ==1:
        graph[x][y] = 0 # visited

        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y) # 십자가 모양으로 반복

        return True # 1일 경우에 True --> 이건 카운트로 연결됨
    
    # else: 생략된 else
    return False #1이 아닐 경우에는 False


T = int(input())
result = []
for i in range(T):
    M, N, K = map(int,input().split())
    graph = [[0]*M for i in range (N)]

    for _ in range(K):
        y, x = map(int,input().split())
        graph[x][y] = 1

    count = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if dfs(i, j):
                    count += 1
    
    result.append(count)

for n in result:
    print(n)

