dishes = list(map(str,input().rstrip()))
# print(dishes)
answer = 10
for i in range(1, len(dishes)):
    if dishes[i] == dishes[i-1]:
        answer += 5
    else :
        answer += 10
        
print(answer)