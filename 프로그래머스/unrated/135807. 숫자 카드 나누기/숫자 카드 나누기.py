# gcd 최소공배수는 math에서 가져오기
from math import gcd

# 배열 속 최소 공배수를 계산
def get_gcd(arr):
    g = arr[0]
    for i in range(len(arr)):
        g = gcd(g, arr[i])
    return g


def solution(arrayA, arrayB):

    answer = 0
    # 각 배열의 최소 공배수 계산
    gA, gB = get_gcd(arrayA), get_gcd(arrayB)

    # 조건에 맞는지 확인
    for b in arrayB:
        # 나누어 떨어지면 중지
        if not b % gA:
            break

        # 나누어 떨어지지 않으면 정답에 추가
    else:
        answer = max(answer, gA)
            
    # 조건에 맞는지 확인
    for a in arrayA:
        # 나누어 떨어지면 중지
        if not a % gB:
            break
            
        
        # 나누어 떨어지지 않으면 정답에 추가
    else:
        answer = max(answer, gB)

    return answer