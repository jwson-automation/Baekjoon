number = int(input())
d = 1
numbers = []
while d <= number:
    numbers.append(d)
    number = number - d
    d = d+1
print(max(numbers))