n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())
    a = e - c
    if r < a:
        print("advertise")
    elif r == a:
        print("does not matter")
    else:
        print("do not advertise")