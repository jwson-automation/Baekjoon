# 최대공약수 함수 가져오기
def gcd(x, y):
    while y:
        x, y = y, x % y
    if x == 1 :
        x = 0
    return x

# 조건에 맞는지 확인하는 함수
def option(gcd_a, array):
    for number in array:
        if gcd_a > number or gcd(gcd_a, number) == 0 :
            return True
        return False

def solution(arrayA, arrayB):

    # A배열의 최대공약수 구하기
    gcd_arrayA = gcd(arrayA[0],arrayA[1])

    for i in range(2, len(arrayA)-1):
        if gcd_arrayA != 0 :
            gcd_arrayA = gcd(gcd_arrayA,arrayA[i])

    # B 배열의 최대공약수 구하기
    gcd_arrayB = gcd(arrayB[0],arrayB[1])

    for i in range(2, len(arrayB)-1):
        if gcd_arrayB != 0 :
            gcd_arrayB = gcd(arrayB,arrayB[i])


    # 조건에 맞다면 정답에 넣어주기
    answer = []

    if(option(gcd_arrayA,arrayB)):
        answer.append(gcd_arrayA)
    if(option(gcd_arrayB,arrayA)):
        answer.append(gcd_arrayB)
    
    if not answer:
        return 0
    return (max(answer))


