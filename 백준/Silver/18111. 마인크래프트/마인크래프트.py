import sys

# 첫째 줄에 Y, X, B가 주어진다. (1 ≤ X, Y ≤ 500, 0 ≤ B ≤ 6.4 × 107)
# 가로, 세로, 인벤토리의 블록 갯수
Y,X,B = map(int,input().split())

answer = []
graph = []

for _ in range (Y) : graph += map(int, input().split())

for number in range (min(graph), max(graph)+1):
    count = 0
    if sum(graph) + B >= Y*X*number:        
        for c_block in graph:
            if c_block > number:
                count += (c_block-number)*2
            elif c_block < number:
                count += (number-c_block)
        answer.append((count,number))

answer = sorted(answer,key = lambda x:x[1], reverse=True)
answer = sorted(answer,key = lambda x:x[0])
# print(answer)
print(answer[0][0],answer[0][1])

# 첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 
# 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.
