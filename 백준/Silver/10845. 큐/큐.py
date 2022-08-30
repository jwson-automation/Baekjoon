from collections import deque
import sys

N = int(sys.stdin.readline())
numbers = deque()

for i in range(N):
    T = sys.stdin.readline().split()
    if T[0] == 'push':
        numbers.append(T[1])
    elif T[0] == 'front':
        if len(numbers) > 0:
            print(numbers[0])
        else: print(-1)
    elif T[0] == 'back':
        if len(numbers) > 0:
            print(numbers[-1])
        else: print(-1)
    elif T[0] == 'size':
        print(len(numbers))
    elif T[0] == 'empty':
        if len(numbers) == 0 :
            print(1)
        else:
            print(0)
    elif T[0] == 'pop':
        if len(numbers) > 0:
            P = numbers.popleft()
            print(P)
        else: print(-1)
