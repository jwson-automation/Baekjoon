import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0
a.sort()
for i in range(n):
    x = a[i]
    y = b.pop(b.index(max(b)))

    answer += x * y
    
print(answer)