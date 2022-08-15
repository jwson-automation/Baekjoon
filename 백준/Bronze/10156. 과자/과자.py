K, N, M = map(int, input().split())

if K * N > M:
    print(K * N - M)
else:
    print(0)