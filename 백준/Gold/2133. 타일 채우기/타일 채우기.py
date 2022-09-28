n = int(input())

dp = [0 for _ in range(32)]

dp[2] = 3 

for i in range(4, n+1, 2):
    dp[i] = 2 + dp[i-2] * 3 + sum(dp[:i-2]) * 2

print(dp[n])

# sum(dp[:i-2])*2 이게 왜 필요한건지를 찾아봤다

# 결론만 말하자면, 곱하고 더한거 +로 가로로 길다란 블록들이 나타난다.

# 그 경우를 더해줘야 하기때문에, 이전 블록들의 모든 경우의수를 더해주는 것

# 설명자료 https://suri78.tistory.com/103

# 그림자료 https://0equal2.tistory.com/114
