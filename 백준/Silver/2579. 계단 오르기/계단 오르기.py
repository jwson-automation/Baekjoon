import sys

n = int(input())
graph = [0]
dp = [0 for _ in range (n+1)]
for _ in range (n):
    graph.append(int(input()))

dp[0] = 0

dp[1] = graph[1]

if n > 1:
    dp[2] = max(graph[2] + graph[1], graph[2] + graph[0])
if n > 2:
    dp[3] = max(graph[3] + graph[2] + graph[0] , graph[3] + graph[1] + graph[0])
if n > 3:    
    for i in range (4,n+1):
        dp[i] = max( graph[i] + graph[i-1] + dp[i-3], graph[i] + dp[i-2] )

print(dp[n])