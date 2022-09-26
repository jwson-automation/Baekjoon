t = int(input())

dp = [[0]*15 for _ in range(15)]


for a in range(0, 15):
    for b in range(0, 15):
        dp[0][b] = b+1
        dp[b][0] = 1
        if dp[a][b] == 0 :
            dp[a][b] = dp[a][b-1] + dp[a-1][b]

for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])
 

# print(dp)
