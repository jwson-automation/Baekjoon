numbers = []
numbers_2 = []
for i in range(5):
    number = int(input())
    numbers.append(number)
    if numbers[i] < 40:
        numbers_2.append(40)
    else:
        numbers_2.append(numbers[i])

print((sum(numbers_2)//5))