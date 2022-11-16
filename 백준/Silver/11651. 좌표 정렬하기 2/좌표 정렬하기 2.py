import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

s_array = sorted(array)

for y, x in s_array:
    print(x, y)
