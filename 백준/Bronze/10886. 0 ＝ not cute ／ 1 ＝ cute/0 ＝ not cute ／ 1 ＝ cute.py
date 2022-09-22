a = int(input())
c = 0

for i in range(a):
    b = int(input())
    if b == 0:
        c -= 1
    else:
        c += 1

if c > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")