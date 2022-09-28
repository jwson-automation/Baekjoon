n, k = map(int,input().split())
c = []
for _ in range(n):
    tmp = int(input())
    c.append(tmp)
dp = [0 for _ in range(k+1)]

# dp[i]에는 dp[i - 1], dp[i - 5], dp[i - 12]중 가장 작은 값에 1을 더해주면 된다.

for i in range(1, k + 1):
    a = [] # 리셋
    for j in c:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])

    if not a: # 안됨
        dp[i] = -1
    else: # 됨
        dp[i] = min(a) + 1

print(dp[k])