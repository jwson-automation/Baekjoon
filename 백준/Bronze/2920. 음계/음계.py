numbers = list(map(int,input().split()))
count = 0

for i in range(7):
    if numbers[i] + 1 == numbers[i+1]:
        count += 1
    elif numbers[i] - 1 == numbers[i+1]:
        count -= 1

if count == 7:
    print('ascending')
elif count == -7:
    print('descending')
else:
    print('mixed')
