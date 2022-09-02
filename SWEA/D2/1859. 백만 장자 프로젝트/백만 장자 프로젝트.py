# import sys
# input = sys.stdin.readline
from collections import deque

n = int(input())

for k in range(n):
    day = int(input())
    price = deque(list(map(int,input().split())))
    price.reverse()
    max = price[0]
    answer = 0
    
    while price:
        if price[0] >= max:
            max = price[0]
            price.popleft()

        elif price [0] < max:
            answer += max - price[0]
            price.popleft()
    
    num = str(k+1)
    print(f'#{num} {answer}')
