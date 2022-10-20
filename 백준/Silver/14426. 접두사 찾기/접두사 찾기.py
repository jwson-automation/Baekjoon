import sys
from bisect import bisect

n, m = map(int,sys.stdin.readline().split())

words = []
answer = []

for _ in range(n):
    words.append(sys.stdin.readline().rstrip())
words.sort()
for _ in range(m):
    key = (sys.stdin.readline().rstrip())
    index = min(n-1, bisect(words,key))
    if words[index].startswith(key):
        answer.append(key)
    elif words[index-1].startswith(key):
        answer.append(key)
        
print(len(answer))