import math
numbers = list(map(int,(input().split())))
answer = 0
for i in numbers:
    answer += i**2
print(answer%10)




