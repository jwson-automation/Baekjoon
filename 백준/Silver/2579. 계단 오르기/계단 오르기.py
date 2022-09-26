import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
stairs = deque()
dp = [0 for _ in range (t+1)]

for _ in range(t):
    temp = int(input())
    stairs.append(temp)

dp[0] = stairs[0]

if t ==1:
    print(dp[0])
    sys.exit(0)

dp[1]=stairs[1]+stairs[0]

if t ==2:
    print(dp[1])
    sys.exit(0)

dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3,t):
    dp[i] = max(dp[i-2]+stairs[i],dp[i-3]+stairs[i-1]+stairs[i])

print(dp[t-1])