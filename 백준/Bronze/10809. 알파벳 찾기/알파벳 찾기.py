word = list(map(str, input().rstrip()))

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alphabet:
    if i not in word:
        print(-1,end=' ')
    elif i in word:
        print(word.index(i), end = ' ')