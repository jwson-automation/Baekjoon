t = int(input())
for _ in range(t):
    n = int(input())

    dp = [0 for i in range(101)]

    dp[0] = 0 # 무시해준다.
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1 
    dp[4] = 2 # 이친구하고
    dp[5] = 2 
    dp[6] = 3 
    dp[7] = 4 
    dp[8] = 5 #이친구를 더하면
    dp[9] = 7 #얘가 나옴
    dp[10] = 9 
    dp[11] = 12 
    for i in range (11, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])

