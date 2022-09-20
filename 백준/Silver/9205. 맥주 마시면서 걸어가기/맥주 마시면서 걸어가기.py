import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())

for i in range(TC):
    convenience = int(input())
    coordinates = []
    for i in range(convenience + 2):
        y , x = map(int,input().split())
        y += 50000
        x += 50000
        coordinates.append((y,x))
    # maxValue = max(map(max, coordinates))
    graph = [[0]*100000]*100000
    list = [[]for _ in range(convenience+2)]
    visited = [0 for _ in range(convenience+2)]


    def inRange(n1, n2, n3, n4):
        if n1 >= n2 and n3 >= n4:
            return 0 <= (n1 - n2) + (n3 - n4)  < 1001
        elif n1 >= n2 and n3 < n4:
            return 0 <= (n1 - n2) + (n4 - n3)  < 1001
        elif n1 < n2 and n3 >= n4:
            return 0 <= (n2 - n1) + (n3 - n4)  < 1001
        elif n1 < n2 and n3 < n4:
            return 0 <= (n2 - n1) + (n4 - n3)  < 1001

    def connection():
        for i in range (len(coordinates)):
            y, x = coordinates[i]
            for j in range(len(coordinates)):
                y1, x1 = coordinates[j]
                if i != j:
                    
                    if inRange(y, y1, x, x1):
                        list[i].append(j)
                        # list[j].append(i)

    connection()
    # print(list)

    def dfs():
        q = deque()
        q.append(0)
        while q:
            tmp = q.popleft()
            visited[tmp] = 1
            for i in list[tmp]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)

    dfs()
    # print(visited)

    if visited[-1] == 1:
        print('happy')
    else : 
        print('sad')