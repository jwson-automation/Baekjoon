n = int(input())
dp = [0 for n in range(n+1)]

graph = [ list(map(int, input().split())) for _ in range (n) ]

for i in range(n):
    if i + graph[i][0] <= n:
        dp[i+graph[i][0]] = max(dp[i+graph[i][0]], dp[i] + graph[i][1])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])