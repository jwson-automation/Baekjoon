import math

def isPrime(x): # 소수 구분! (절반까지 나눠보기)
    for i in range (2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

n = int(input())
result = 0

for i in range(n,1000001):#최대값까지 돌려주는데
    if i == 1: # 1은 소수가 아니라서 무시 (*소수는 2부터임)
        continue
    if str(i) == str(i)[::-1]: # 펠린드롬이어야하고
        if isPrime(i): #소수여야해
            result = i #맞으면 출력해조
            break # 그리고 끝내줘
if result == 0: # 100만 이상인 경우의 반례
    result = 1003001 

print(result)



