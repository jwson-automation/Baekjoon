from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())

    dp = [0 for _ in range(n+1)]
    dp[0] = 0


    q = deque()
    q.append(0)
    while q:
        # print(q)
        k = q.popleft()
        if 0<= k+1 < n+1 :
            dp[k+1] += 1
            q.append(k+1)
        if 0<= k+2 < n+1 :
            dp[k+2] += 1
            q.append(k+2)
        if 0<= k+3 < n+1 :
            dp[k+3] += 1
            q.append(k+3)

    print(dp[n])