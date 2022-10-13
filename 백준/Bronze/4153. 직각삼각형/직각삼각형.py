import sys
while True:
    a, b, c = map(int,input().split())
    if a == b == c == 0:
        sys.exit()
    a = a**2
    b = b**2
    c = c**2
    if a + b == c or b + c == a or c + a == b:
        print('right')
    else: print('wrong')
    