numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if a != b != c != a:
    print(int(max(numbers))*100)
elif a == b == c == a:
    print(a*1000+10000)
elif c == a != b:
    print(a*100+1000)
elif a == b != c:
    print(a*100+1000)
elif b == c != a:
    print(b*100+1000)