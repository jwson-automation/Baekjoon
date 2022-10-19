n = int(input())
numbers = list(map(int,input().split()))
count = 0

def is_prime_number(x):
    if x != 1:
        for i in range(2,x):
            if x%i == 0:
                return False
        return True
    else:
        return False

for k in numbers:
    if is_prime_number(k):
        count += 1

print(count)