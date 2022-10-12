import sys

ty, tx = map(int,input().split())

graph = []

for i in range(ty):
    graph.append(list(input()))

result = [sys.maxsize]
# 8개씩 쪼개서 생각하기
for y in range(ty-7):
    for x in range(tx-7):

        count = 0
        # W시작
        if graph[y][x] == 'W':
            for y2 in range (y, y+8):
                for x2 in range (x, x+8):
                    if ((y2+x2)%2 != 0 and graph[y2][x2] == 'W'):
                        count += 1
                    if ((y2+x2)%2 == 0 and graph[y2][x2] == 'B'):
                        count += 1
            
            
        # B시작
        else :
            for y2 in range (y, y+8):
                for x2 in range (x, x+8):
                    if ((y2+x2)%2 != 0 and graph[y2][x2] == 'B'):
                        count += 1
                    if ((y2+x2)%2 == 0 and graph[y2][x2] == 'W'):
                        count += 1

        result.append(count)
        count = 0

        if graph[y][x] == 'W':
            # graph[y][x] = 'B'
            # count += 1
            for y2 in range (y, y+8):
                for x2 in range (x, x+8):
                    if ((y2+x2)%2 != 0 and graph[y2][x2] == 'B'):
                        count += 1
                    if ((y2+x2)%2 == 0 and graph[y2][x2] == 'W'):
                        count += 1
            

        else : 
            # graph[y][x] = 'W'
            # count += 1
            for y2 in range (y, y+8):
                for x2 in range (x, x+8):
                    if ((y2+x2)%2 != 0 and graph[y2][x2] == 'W'):
                        count += 1
                    if ((y2+x2)%2 == 0 and graph[y2][x2] == 'B'):
                        count += 1
            # here

        result.append(count)
        count = 0

        if graph[y+7][x+7] == 'W':
            for y2 in range (y+7, y-1, -1):
                for x2 in range (x+7, x-1, -1):
                    if ((y2+x2)%2 != 0 and graph[y2][x2] == 'W'):
                        count += 1
                    if ((y2+x2)%2 == 0 and graph[y2][x2] == 'B'):
                        count += 1
            

        # B시작
        else :
            for y2 in range (y+7, y-1, -1):
                for x2 in range (x+7, x-1, -1):
                    if ((y2+x2)%2 != 0 and graph[y2][x2] == 'B'):
                        count += 1
                    if ((y2+x2)%2 == 0 and graph[y2][x2] == 'W'):
                        count += 1

            

        result.append(count)
        count = 0

        if graph[y+7][x+7] == 'W':
            # graph[y][x] = 'B'
            # count += 1
            for y2 in range (y+7, y-1, -1):
                for x2 in range (x+7, x-1, -1):
                    if ((y2+x2)%2 != 0 and graph[y2][x2] == 'W'):
                        count += 1
                    if ((y2+x2)%2 == 0 and graph[y2][x2] == 'B'):
                        count += 1
        else : 
            # graph[y][x] = 'W'
            # count += 1
            for y2 in range (y+7, y-1, -1):
                for x2 in range (x+7, x-1, -1):
                    if ((y2+x2)%2 != 0 and graph[y2][x2] == 'B'):
                        count += 1
                    if ((y2+x2)%2 == 0 and graph[y2][x2] == 'W'):
                        count += 1

        result.append(count)

    
# print(result)
print(min(result))
            