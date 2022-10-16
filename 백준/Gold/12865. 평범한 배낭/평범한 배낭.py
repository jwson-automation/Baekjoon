import sys

input = sys.stdin.readline
n, k  = map(int, input().split())
items = []
# y축 = 물건의 무게, 가치  / x축 = 배낭의 무게
# +1 달아서 0,0은 0으로 추가 (물건을 못넣을 때)
dp = [[0]*(k+1) for _ in range(n+1)]

for y in range(1, n+1): # 물건이 
    weight, value = map(int,input().split())
    for x in range (1, k+1): # 가방 무게가 x일 때
        # 물건을 담을 수 있을 때 (x보다  무게가 작거나 같을 때)
        if x < weight :
            dp[y][x] = dp[y-1][x]
       
        # 물건을 담을 수 없을 때 ( 전에 넣어뒀던 무게로 유지)
        else:
            dp[y][x] = max(dp[y-1][x],dp[y-1][x-weight] + value )


print(dp[n][k])

