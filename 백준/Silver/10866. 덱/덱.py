import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    command = list(input().split())
    # push_front X: 정수 X를 덱의 앞에 넣는다.
    if command[0] =='push_front':
        q.appendleft(int(command[1]))

    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif command[0] =='push_back':
        q.append(int(command[1]))

    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] =='pop_front':
        if not q:
            print(-1)
        else : 
            k = q.popleft()
            print(k)

    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] =='pop_back':
        if not q:
            print(-1)
        else :
            k = q.pop()
            print(k)
        
    # size: 덱에 들어있는 정수의 개수를 출력한다.
    elif command[0] == 'size':
        print(len(q))
    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif command[0] == 'empty' :
        if not q:
            print(1)
        else: print(0)

    # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] =='front':
        if not q:
            print(-1)
        else : print(q[0])

    # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command[0] =='back':
        if not q:
            print(-1)
        else : print(q[-1])