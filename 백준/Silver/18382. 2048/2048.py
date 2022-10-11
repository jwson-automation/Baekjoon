import sys
from collections import deque

input = sys.stdin.readline

# 입력 모두 넣어주기
score = int(input())
command = deque(list(input().rstrip()))
grid = deque(list(map(int,input().split())))

# 그래프로 만들기
graph = [deque(),deque(),deque(),deque()]
for a in range(4):
    for b in range(4):
        k = grid.popleft()
        graph[a].append(k)

# print(graph)

def same(y2,x2,y,x):
    return graph[y2][x2] == graph[y][x]

def zero(y,x):
    return graph[y][x] == 0

# 먼저 그리드 이동을 함수로 생성
def movement(direction):
    global score
    if direction == 'R': # 오른쪽 방향이 가장 쉬움 평범
        #밀기 (정방향 + 역방향 2번 0을 없애준다.)
        for y in range (4):
            for x in range (3):
                if graph[y][x] != 0 and zero(y, x+1):
                    graph[y][x+1] = graph[y][x]
                    graph[y][x] = 0
            for x in range (3,0,-1):
                if graph[y][x] == 0 and not zero(y, x-1):
                    graph[y][x] = graph[y][x-1]
                    graph[y][x-1] = 0
        #합치기
            for x in range(3,0,-1):
                if graph[y][x] != 0 and same(y,x,y,x-1):
                    graph[y][x] += graph[y][x-1]
                    score += graph[y][x]
                    graph[y][x-1] = 0
        #다시 밀기 (위 코드대로하면, 2422 일때 반례가 생김)
            for x in range (3):
                if graph[y][x] != 0 and zero(y, x+1):
                    graph[y][x+1] = graph[y][x]
                    graph[y][x] = 0
            for x in range (3,0,-1):
                if graph[y][x] == 0 and not zero(y, x-1):
                    graph[y][x] = graph[y][x-1]
                    graph[y][x-1] = 0           
                
    if direction == 'L': #오른쪽 방향을 방향만 바꿔주면 오케이!
        #밀기 (정방향 + 역방향 2번 0을 없애준다.)
        for y in range (4):
            for x in range (3):
                if graph[y][x] == 0 and not zero(y, x+1):
                    graph[y][x] = graph[y][x+1]
                    graph[y][x+1] = 0
            for x in range (3,0,-1):
                if graph[y][x] != 0 and zero(y, x-1):
                    graph[y][x-1] = graph[y][x]
                    graph[y][x] = 0
        #합치기(반대방향임으로 역순으로 해준다)
            for x in range(3):
                if graph[y][x] != 0 and same(y,x,y,x+1):
                    graph[y][x] += graph[y][x+1]
                    score += graph[y][x]
                    graph[y][x+1] = 0
        #다시 밀기 (위 코드대로하면, 2422 일때 반례가 생김)
            for x in range (3):
                if graph[y][x] == 0 and not zero(y, x+1):
                    graph[y][x] = graph[y][x+1]
                    graph[y][x+1] = 0
            for x in range (3,0,-1):
                if graph[y][x] != 0 and zero(y, x-1):
                    graph[y][x-1] = graph[y][x]
                    graph[y][x] = 0
                
    if direction == 'D': # y,x의 축을 바꿔준다
        #밀기 (정방향 + 역방향 2번 0을 없애준다.)
        for x in range (4):
            for y in range (3):
                if graph[y][x] != 0 and zero(y+1,x):
                    graph[y+1][x] = graph[y][x]
                    graph[y][x] = 0
            for y in range (3,0,-1):
                if graph[y][x] == 0 and not zero(y-1,x):
                    graph[y][x] = graph[y-1][x]
                    graph[y-1][x] = 0
        #합치기
            for y in range(3,0,-1):
                if graph[y][x] != 0 and same(y-1,x,y,x):
                    graph[y][x] += graph[y-1][x]
                    score += graph[y][x]
                    graph[y-1][x] = 0
        #다시 밀기 (위 코드대로하면, 2422 일때 반례가 생김)
            for y in range (3):
                if graph[y][x] != 0 and zero(y+1,x):
                    graph[y+1][x] = graph[y][x]
                    graph[y][x] = 0
            for y in range (3,0,-1):
                if graph[y][x] == 0 and not zero(y-1,x):
                    graph[y][x] = graph[y-1][x]
                    graph[y-1][x] = 0

    if direction == 'U':
        #밀기 (정방향 + 역방향 2번 0을 없애준다.)
        for x in range (4):
            for y in range (3):
                if graph[y][x] == 0 and not zero(y+1, x):
                    graph[y][x] = graph[y+1][x]
                    graph[y+1][x] = 0
            for y in range (3,0,-1):
                if graph[y][x] != 0 and zero(y-1, x):
                    graph[y-1][x] = graph[y][x]
                    graph[y][x] = 0
        #합치기(반대방향임으로 역순으로 해준다)
            for y in range(3):
                if graph[y][x] != 0 and same(y,x,y+1,x):
                    graph[y][x] += graph[y+1][x]
                    score += graph[y][x]
                    graph[y+1][x] = 0
        #다시 밀기 (위 코드대로하면, 2422 일때 반례가 생김)
            for y in range (3):
                if graph[y][x] == 0 and not zero(y+1, x):
                    graph[y][x] = graph[y+1][x]
                    graph[y+1][x] = 0
            for y in range (3,0,-1):
                if graph[y][x] != 0 and zero(y-1, x):
                    graph[y-1][x] = graph[y][x]
                    graph[y][x] = 0
     

#숫자 생성도 함수로 분리해줌
def creation(number, y, x):
    if graph[y][x] != 0:
        print('error!')
    graph[y][x] = number

# 명령어도 따로 구분해주겠음
for i in range(len(command)):
    if i % 4 == 0:
        tmp = command.popleft()
        movement(tmp)
    elif i % 4 == 1:
        create_number = int(command.popleft())
    elif i % 4 == 2:
        y = int(command.popleft())
    elif i % 4 == 3:
        x = int(command.popleft())
        creation(create_number, y,x)

# print(graph)
print(score)