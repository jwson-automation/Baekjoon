import sys
from collections import deque
input = sys.stdin.readline

hills = int(input())
elevation = []
for i in range (hills):
    elevation.append([int(input()), int(i)])

count = deque([0 for _ in range (hills)])

def sorting():
    return elevation.sort(reverse=True, key=lambda x : x[0])

def value():
    tmp = []
    for i in range(len(elevation)):
        tmp.append(elevation[i][0])
    tmp_max = max(tmp)
    tmp_min = min(tmp)
    return tmp.count(tmp_min) >= tmp.count(tmp_max)
    
maxValue = 100
minValue = 5

while (maxValue - minValue) > 17 :
    sorting()
    if value():
        elevation[0][0] -= 1
        count[elevation[0][1]] += 1
        sorting()
    else :
        elevation[-1][0] += 1
        count[elevation[-1][1]] += 1
        sorting()
    maxValue = (max(elevation, key=lambda x: x[0]))[0]
    minValue = (min(elevation, key=lambda x: x[0]))[0]

answer = 0
while count:
    k = count.popleft()
    if k != 0:
        answer += k**2

print(answer)
    

