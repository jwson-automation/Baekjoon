n = int(input())

g = []
for _ in range (n):
    g += list(map(int,input().split()))

dp = [0]*(n*n)
dp[0] = 1 
g[-1] = 1

for t in range(n*n):
    if dp[t] != 0 or t == 0 :
        m = g[t]
        if  m + t%n <n:
            dp[m + t] += dp[t]

        if m + t//n < n:
            dp[((t//n + m)*n) + t%n] += dp[t]
            
print(dp[(n*n)-1])
