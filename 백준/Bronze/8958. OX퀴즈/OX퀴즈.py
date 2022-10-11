import sys

t = int(input())

for _ in range (t):
    count = 0
    bonus = 0
    ox = list(input().rstrip())
    if ox[0] == 'O':
        count += 1
    for i in range(1, len(ox)):
        if ox[i-1] == 'O':
            bonus += 1
        elif ox[i-1] == 'X':
            bonus = 0
        if ox[i] == 'O':
            count += 1 + bonus
        
    bonus = 0
    print(count)


        
    

