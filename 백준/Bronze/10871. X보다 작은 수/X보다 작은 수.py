n, x  = map (int,input().split())

# n개
numbers = list(map(int,input().split()))

for i in numbers : 
    if i < x:
        print(i, end = ' ')
