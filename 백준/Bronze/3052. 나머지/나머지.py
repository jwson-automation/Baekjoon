answer = []
for _ in range(10):
    a = int(input())
    if a%42 not in answer :
        answer.append(a%42)
print(len(answer))