n = int(input())


numbers = [list(map(str,input().split())) for _ in range (n)]
    
answer = 0

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            #각 케이스 마다 볼카운트, 스트라이크 카운트 확인
            tmp = 0
            
            # 서로 다른 세 자리수
            if (a == b or b == c or c == a):
                # print(str(a)+str(b)+str(c))
                continue

            # 조건 대입하기
            for array in numbers:
                check = list(array[0])
                strike = int(array[1])
                ball = int(array[2])
                ball_count = 0
                strike_count = 0

                #스트라이크 계산기
                if (a == int(check[0])):
                    strike_count += 1
                if (b == int(check[1])):
                    strike_count += 1
                if (c == int(check[2])):
                    strike_count += 1
                if (strike != strike_count):
                    break

                #볼 계산기
                if (a == int(check[1]) or a == int(check[2])):
                    ball_count +=  1
                if (b == int(check[0]) or b == int(check[2])):
                    ball_count +=  1
                if (c == int(check[0]) or c == int(check[1])):
                    ball_count +=  1
                if (ball != ball_count):
                    break

                #일치하면 더해주기
                tmp += 1
            if tmp == n:
                answer += 1
                
print(answer)

