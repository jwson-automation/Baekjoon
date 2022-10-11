import sys
input = sys.stdin.readline
word = list(map(str, input().rstrip().upper()))
answer = [(0,0)]
used_alphabet = []

if len(word) == 1:
    print(word[0])
    sys.exit()

for i in (word):
    if i in used_alphabet:
        continue
    used_alphabet.append(i)
    count = word.count(i)
    answer.append((count, i))

answer.sort(reverse=True)
if answer[0][0] == answer[1][0]:
    print('?')
else:
    print(max(answer)[1])



