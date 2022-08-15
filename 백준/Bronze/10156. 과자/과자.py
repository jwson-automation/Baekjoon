numbers = input().split()
price = int(numbers[0])
howmany = int(numbers[1])
money = int(numbers[2])
needMoney = int(money-(price*howmany))

if needMoney >= 0:
    print(0)
elif needMoney < 0:
    print(needMoney*-1)
