import sys
input = sys.stdin.readline

# 입력
n = int(input())
numbers = list(map(int,input().split()))

# DP
dp = [[0 for _ in range (n)] for _ in range(n)]

# y축이 시작, x축이 완료
for tmp in range(n):
    for y in range(n-tmp):
        x = y + tmp
        if y == x:
            dp[y][x] = 1
        # 여기가 가장 중요하다, 양끝이 다르면 일단 땡임
        elif numbers[y] == numbers[x]:
            if dp[y+1][x-1] == 1:
                dp[y][x] = 1
            elif numbers[y:x+1] == numbers[y:x+1][::-1]:
                dp[y][x] = 1

# 질문 갯수
q = int(input())
for _ in range(q):
    # 시작과 끝을 입력 받아서
    start, end = map(int,input().split())
    #정답 출력
    print(dp[start-1][end-1])