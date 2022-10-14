n = int(input())

graph = []
for _ in range (n):
    graph += list(map(int,input().split()))
# print(graph)

dp = [0]*(n*n)
dp[0] = 1 
graph[-1] = 1

for cur_number in range(n*n):
    if dp[cur_number] != 0 or cur_number == 0 :
        # print(cur_number)
        moving_number = graph[cur_number]
        # x축 그냥 더하기
        if  moving_number + cur_number%n <n:
            dp[moving_number + cur_number] += dp[cur_number]

        # y축 n만큼 곱하기
        if moving_number + cur_number//n < n:
            dp[((cur_number//n + moving_number)*n) + cur_number%n] += dp[cur_number]
            
        

# print(dp)
print(dp[(n*n)-1])
