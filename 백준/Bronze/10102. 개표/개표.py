n = input()
score = list(input())
a = score.count('A')
b = score.count('B')
if a == b:
    print('Tie')
elif a > b:
    print('A')
else:
    print('B')