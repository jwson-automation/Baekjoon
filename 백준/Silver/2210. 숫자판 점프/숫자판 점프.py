graph = []
result = []

for _ in range (5):
    graph.append(list(map(str,input().split())))


def inRange(A):
    if (A >= 0 and A < 5) : return True
    return False

def dfs(x,y,number):
    if len(number) == 6:
        result.append(number)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if inRange(nx) and inRange(ny):
            dfs(nx , ny, number + graph[nx][ny])
    



for a in range (5):
    for b in range(5):
        dfs(a,b,graph[a][b])


# print(set(result))
print(len(set(result)))