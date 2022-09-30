t = int(input())
dp = [[0 for _ in range(3)] for _ in range(t+1)]

# print(dp)

graph = [list(map(int,input().split())) for _ in range(t)]
dp[1][0] = graph[0][0]
dp[1][1] = graph[0][1]
dp[1][2] = graph[0][2]

dp[2][0] = min(graph[0][1] + graph[1][0],graph[0][2] + graph[1][0])
dp[2][1] = min(graph[0][0] + graph[1][1],graph[0][2] + graph[1][1])
dp[2][2] = min(graph[0][0] + graph[1][2],graph[0][1] + graph[1][2])

for i in range(2, t+1):
    dp[i][0] = min(dp[i-1][1] + graph[i-1][0], dp[i-1][2] + graph[i-1][0])
    dp[i][1] = min(dp[i-1][0] + graph[i-1][1], dp[i-1][2] + graph[i-1][1])
    dp[i][2] = min(dp[i-1][0] + graph[i-1][2], dp[i-1][1] + graph[i-1][2])

print(min(dp[t])) 