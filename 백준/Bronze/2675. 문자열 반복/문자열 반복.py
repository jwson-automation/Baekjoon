T = int(input())
for i in range(T):
    hi = input().split()
    number = int(hi[0])
    word = list(str(hi[1]))
    for i in range(len(word)):
        print(word[i]*number, end='')
    print("")





