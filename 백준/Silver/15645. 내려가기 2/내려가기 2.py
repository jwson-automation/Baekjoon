from copy import deepcopy

A = int(input())
numbers = [ [] for _ in range (0,A)]


for i in range (0, A):
    B,C,D = map(int,input().split())
    numbers[i].append(B)
    numbers[i].append(C)
    numbers[i].append(D)

numbers2 = deepcopy(numbers)


for x in range (1, A):
    numbers[x][0] = max(numbers[x-1][0], numbers[x-1][1]) + numbers[x][0]

    numbers[x][1] = max(numbers[x-1][0], numbers[x-1][1], numbers[x-1][2]) +  numbers[x][1]

    numbers[x][2] = max(numbers[x-1][1], numbers[x-1][2]) + numbers[x][2]



for x in range (1, A):
    numbers2[x][0] = min(numbers2[x-1][0], numbers2[x-1][1]) + numbers2[x][0]

    numbers2[x][1] = min(numbers2[x-1][0], numbers2[x-1][1], numbers2[x-1][2]) +  numbers2[x][1]

    numbers2[x][2] = min(numbers2[x-1][1], numbers2[x-1][2]) + numbers2[x][2]

print(max(numbers[A-1][0],numbers[A-1][1],numbers[A-1][2]), min(numbers2[A-1][0],numbers2[A-1][1],numbers2[A-1][2]))