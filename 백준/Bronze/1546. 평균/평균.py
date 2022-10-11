n = int(input())
numbers = list(map(int,input().split()))
numbers.sort(reverse=True)
for i in range(1,n):
    numbers[i] = numbers[i]/numbers[0]*100
numbers[0] = 100
print(sum(numbers)/n)




