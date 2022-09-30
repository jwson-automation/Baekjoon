from collections import deque

n = int(input())

dp = [10**6 for _ in range(n+1)]
dp[n] = 0

for i in range(n):
    q = deque()
    q.append(n)
    while q:
        k = q.popleft()
        if k%2 == 0 and 0 < k//2 < n and dp[k//2] > dp[k] + 1:
            dp[k//2] = dp[k] + 1
            q.append(k//2)
        if k%3 == 0 and 0 < k//3 < n and dp[k//3] > dp[k] + 1:
            dp[k//3] = dp[k] + 1
            q.append(k//3)
        if 0< k-1 < n and dp[k-1] > dp[k] + 1:
            dp[k-1] = dp[k] + 1
            q.append(k-1)

print(dp[1])