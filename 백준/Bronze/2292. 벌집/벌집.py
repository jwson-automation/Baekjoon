import sys
n = int(input())

# if n == 1:
#     print(0)
#     sys.exit()

cnt = 1

tmp = 6

answer = 1

#경계값을 늘려주면서 6씩 더해준다
while n > cnt:

    answer += 1

    cnt += tmp

    tmp += 6
    
print(answer)

# 1
# 2 ~ 7 6 1
# 8 ~ 19 12 2
# 20 ~ 37 18 3
# 38 ~ 61 24 4
