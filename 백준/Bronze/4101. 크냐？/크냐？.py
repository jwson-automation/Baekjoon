nA = []
nB = []
k = -1
while True:
    A, B = map(int,input().split())
    nA.append(A)
    nB.append(B)
    k = k +1
    if nA[k] == 0 and nB[k] ==0:
        break

for i in range(0,len(nA)):
    if nA[i] < nB[i]:
        print('No')
    elif nB[i] < nA[i]:
        print('Yes')
    elif nA[i] == nB[i] == 0 :
        continue
    else:
        print('No')