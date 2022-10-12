import sys
input = sys.stdin.readline

tmp = [0] * 10001
for i in range(int(input())):
    tmp[int(input())] += 1

for i in range(10001):
    for _ in range(tmp[i]):
        print(i)