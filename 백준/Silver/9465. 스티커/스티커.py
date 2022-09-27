import sys

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range (2)]
    dp =[[0 for i in range((n+1))] for i in range (2) ]
    
    if n == 0:
        dp[0][0] = 0
        dp[1][0] = 0
        print(0)
        sys.exit()
    if n >= 1:
        dp[0][1] = graph[0][0] 
        dp[1][1] = graph[1][0]
        
    if n >= 2:
        dp[0][2] = graph[1][0] + graph[0][1]
        dp[1][2] = graph[0][0] + graph[1][1]

    if n >= 3:
        for i in range(3, n+1):
            if dp[0][i] == 0:
                dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + graph[0][i-1]
                dp[1][i] = max(dp[0][i-1], dp[1][i-2], dp[0][i-2]) + graph[1][i-1]

    # print(dp)
    print(max(max(dp[0]),max(dp[1])))
    


