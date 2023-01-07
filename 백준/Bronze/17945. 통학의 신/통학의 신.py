A, B = map(int,input().split())
answerBox = []
for x in range(-1000, 1000):
    if((x*x) + (2*A*x) + B == 0):
        answerBox.append(x)

for answer in answerBox:
    print(answer, end=" ")
