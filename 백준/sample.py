
A = int(input())
numbers = []
answer =[]
box = []
n2 = []
n3 = []
n4 = []

for i in range (0, A):
    B,C,D = map(int,input().split())
    numbers.append([B])
    numbers.append([C])
    numbers.append([D])

if A == 1:
    print(max(numbers)[0], min(numbers)[0])
    

else:
    for i in range (3, 6):
        if i % 3 ==0:
            box = [sum(numbers[i]+numbers[i-3]), sum(numbers[i]+numbers[i-2])]
            numbers[i] = box
        elif i % 3 ==1:
            box = [sum(numbers[i]+numbers[i-4]),sum(numbers[i]+numbers[i-3]), sum(numbers[i]+numbers[i-2])]
            numbers[i] = box
        elif i % 3 ==2:
            box = [sum(numbers[i]+numbers[i-4]),sum(numbers[i]+numbers[i-3])]
            numbers[i] = box

    for i in range (3, A*3-3):
        for k in range (0, len(numbers[i])):
            if i %3 ==0:
                n3.append(numbers[i][k]+numbers[i+3][0])
                n4.append(numbers[i][k]+numbers[i+4][0])
            elif i%3 ==1:
                n2.append(numbers[i][k]+numbers[i+2][0])
                n3.append(numbers[i][k]+numbers[i+3][0])
                n4.append(numbers[i][k]+numbers[i+4][0])
                numbers[i+4].append(min(n4))
                numbers[i+4].append(max(n4))
            elif i%3 ==2:
                n2.append(numbers[i][k]+numbers[i+2][0])
                n3.append(numbers[i][k]+numbers[i+3][0])
                numbers[i+2].append(max(n2))
                numbers[i+2].append(min(n2))
                numbers[i+3].append(min(n3))
                numbers[i+3].append(max(n3))
                

    answer.append(max(numbers[A*3-1]))
    answer.append(max(numbers[A*3-2]))
    answer.append(max(numbers[A*3-3]))
    answer.append(min(numbers[A*3-1]))
    answer.append(min(numbers[A*3-2]))
    answer.append(min(numbers[A*3-3]))
    print(max(answer),min(answer))