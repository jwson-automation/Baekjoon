from collections import deque

T = int(input())
for tc in range (1, T+1):
    n = int(input())
    if n == 1:
        print('#{}'.format(tc))
        print(1)
        continue
    numbers = deque([i for i in range (1, (n*n)+1)])
    answer = [[0 for _ in range(n)] for i in range(n)]
    count = n
    y = 0
    x = 0
    vector = 'left'
    while numbers:
        k = numbers.popleft()
        if vector == 'left':
            answer[y][x] = k
            x += 1
            if answer[y][count-1] != 0:
                vector = 'down'
                x -= 1
        if vector == 'down':
            answer[y][x] = k
            y += 1
            if answer[count-1][x] != 0:
                vector = 'right'
                y -= 1
        if vector == 'right':
            answer[y][x] = k
            x -= 1
            if answer[y][n-count] != 0:
                count -= 1
                vector = 'up'
                x += 1
        if vector == 'up':
            answer[y][x] = k
            y -= 1
            if answer[n-count][x] != 0:
                vector = 'left'
                y += 1
                x += 1
    print('#{}'.format(tc))
    for a in range (n):
        for b in range(n):
            if b+1 == n:
                print(answer[a][b])
            else :
                print(answer[a][b], end=' ')