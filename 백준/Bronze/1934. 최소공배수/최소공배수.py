from math import gcd


howmanytime = int(input())
n1 = []
n2 = []
for i in range(howmanytime):
    box1 = input().split()
    n1.append(box1[0])
    n2.append(box1[1])    

for i in range(howmanytime):
    a = int(n1[i])
    b = int(n2[i])
    k = gcd(a, b)
    print(int(a*b/k))        