import math

t = int(input())
for _ in range(t):
    n = int(input())
    answer = 0
    for i in range(1,n+1):
        answer += math.log10(i)
    print(int(answer +1))