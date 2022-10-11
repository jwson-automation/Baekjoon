import sys

while True :
    a, b = map(int,input().split())
    if a == b == 0:
        sys.exit()
    print(a+b)
    