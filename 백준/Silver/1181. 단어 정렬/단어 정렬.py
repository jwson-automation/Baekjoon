words = []
for _ in range(int(input())):
    tmp = input()
    tmp_l = len(tmp)
    words.append((tmp_l, tmp))

words.append((100000000,'dummy'))
words.sort()
# print(words)

for i in range(len(words)-1):
    if words[i] == words[i+1]:
        continue
    else :
        print(words[i][1])

