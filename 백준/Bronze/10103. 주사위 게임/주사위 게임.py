n = int(input())

c = 100
s = 100

for _ in range(n):
    chang, sang = map(int, input().split())
    
    if chang > sang :
        s -= chang
    elif sang > chang :
        c -= sang
    

print(c)
print(s)