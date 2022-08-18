
A = int(input())
numbers = []
n1 = []
n2 = []
n3 = []
answer =[]
p1 = []
p2 = []
p3 = []
score = int(0)

for i in range (0, A):
    B,C,D = map(int,input().split())
    n1.append(B)
    n2.append(C)
    n3.append(D)

score_n1 = n1[0]
score_n2 = n2[0]
score_n3 = n3[0]

for i in range (0, A):
    
    if i%3 == 0:
        k1 = score_n1 + n1[i+1]

        k2 = score_n1 + n2[i+1]
    if i%3 == 1:
        k3 = score_n2 + n1[i+1]

        k4 = score_n2 + n2[i+1]

        k5 = score_n2 + n3[i+1]
    if i%3 == 2:
        k6 = score_n3 + n2[i+1]

        k7 = score_n3 + n3[i+1]
