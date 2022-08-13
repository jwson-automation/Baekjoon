A, B = map(int, input().split())
numbers = []


if A < B:
    print(B-A-1)
    while A < B-1:
        A = A+1
        numbers.append(A)
    for i in range (0, len(numbers)):
        print(numbers[i], end =' ')

elif A == B:
    print(0)

else:
    print(A-B-1)
    while B < A-1:
        B = B+1
        numbers.append(B)
    for i in range (0, len(numbers)):
        print(numbers[i], end =' ')
