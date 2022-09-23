n = int(input())

graph = [[] for i in range(n)]
answer = []

for i in range(n):
    graph[i] = list(map(int, input().split()))
    if graph[i][0] == graph[i][1] == graph[i][2]:
        answer.append((max(graph[i])*1000)+10000)
    elif graph[i][0] == graph[i][1] or graph[i][1] == graph[i][2]:
        answer.append((graph[i][1]*100)+1000)
    elif graph[i][0] == graph[i][2]:
        answer.append((graph[i][0]*100)+1000)
    else:
        answer.append((max(graph[i])*100))
    
print(max(answer))
