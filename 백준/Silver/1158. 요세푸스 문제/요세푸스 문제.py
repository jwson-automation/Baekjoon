from collections import deque
N, K = map(int, input().split())
queue = deque([i for i in range(1,N+1)])
answer = []
i = 0
while queue:
    i += 1
    tmp = queue.popleft()
    if i%K != 0:
        queue.append(tmp)
        # print(queue)
    else:
        answer.append(tmp)
        # print(answer)

# print(queue)
s = ", ".join(map(str, answer)) # 리스트 꺼내기
print('<' + s + '>')
                                                                