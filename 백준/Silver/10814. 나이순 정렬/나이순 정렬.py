t = int(input())
inputList = [[0] for i in range(t)]

for i in range(t):
    A, B = map(str, input().split())
    inputList[i] = [A, B]

inputList.sort(key=lambda x:int(x[0]))

for answer in inputList:
    print(f"{answer[0]} {answer[1]}")
