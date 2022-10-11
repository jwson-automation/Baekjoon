number = 1
for _ in range(3):
    number *= int(input())

numbers = list(map(int, str(number).rstrip()))

for i in range(10):
    print(numbers.count(i))