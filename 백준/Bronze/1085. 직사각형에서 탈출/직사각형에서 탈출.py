y,x,ly,lx = map(int,input().split())

graph = [[0] * x for _ in range(y)]

# 한수는 지금 y,x 에 있다.
# 경계선 까지 가는 거리의 최솟값을 구해랏

answer = []
answer.append(y)
answer.append(x)
answer.append(lx - x)
answer.append(ly - y)

print(min(answer))


