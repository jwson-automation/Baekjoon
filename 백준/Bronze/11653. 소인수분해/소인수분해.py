numbers = int(input())
d = 2
while d <= numbers: 
    if numbers % d == 0: 
        print(d) 
        numbers = numbers / d 
    else: 
        d = d + 1