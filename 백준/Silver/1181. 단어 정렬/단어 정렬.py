n = int(input())

words = []

for i in range(n):
    words.append(input())

setw = set(words)
words = list(setw)
words.sort()
words.sort(key=len)

for i in (words):
    print(i)