n = int(input())
numbers = []
answer = []
count = 1
temp = True

for i in range(n):
    num = int(input())

    while count <= num:
        numbers.append(count)
        answer.append('+')
        count += 1

    if numbers[-1] == num:
        numbers.pop()
        answer.append('-')
        
    else:
        temp = False

if temp == False:
    print('NO')

else:
    for i in answer:
        print(i)