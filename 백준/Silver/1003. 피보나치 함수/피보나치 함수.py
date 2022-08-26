T = int(input())

for i in range (0,T):
    N = int(input())
    answer = [[0,0] for _ in range(N+2)]
    answer[0][0] = answer[1][1] = 1
    answer[0][1] = answer[1][0] = 0

    def fibonacci(n):
        if n > 1 :
            for i in range (2, n+1):
                answer[i][0] = answer[i-1][0] + answer[i-2][0]
                answer[i][1] = answer[i-1][1] + answer[i-2][1]

        print(answer[n][0],answer[n][1])

    fibonacci(N)
