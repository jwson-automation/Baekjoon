T = int(input())
for i in range(T):
    hi = input().split()
    number = float(hi[0])
    for i in range(len(hi)):
        if hi[i] == "@":
            number = number*3
        elif hi[i] == "#":
            number = number-7
        elif hi[i] == "%":
            number = number+5
    print("{:.2f}".format(number))

