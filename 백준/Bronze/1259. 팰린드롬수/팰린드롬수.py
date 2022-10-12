import sys

while True:
    word = list(str(input()))
    if word == ['0']:
        sys.exit()    
    if word == word[::-1]:
        print('yes')
    else :
        print('no')