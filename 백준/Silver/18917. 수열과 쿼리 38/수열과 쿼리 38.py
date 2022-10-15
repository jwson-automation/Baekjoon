import sys

input = sys.stdin.readline

m = int(input())
_sum = 0
_xor = 0
for _ in range(m):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        _sum += tmp[1]
        _xor ^= tmp[1]
    elif tmp[0] == 2:
        _sum -= tmp[1]
        _xor ^= tmp[1]
    elif tmp[0] == 3:
        print(_sum)
    elif tmp[0] == 4:
        print(_xor)