import sys
input = sys.stdin.readline

# 변수 설정
n = int(input())
arr = []
y_list = []
x_list = []
ans = [-1] * n

for _ in range(n):
# 입력
    a, b = map(int,input().split())
    arr.append((a,b))
    y_list.append(b)
    x_list.append(a)

# 모든 지정 좌표 경우의 수 반복
for y in y_list:
    for x in x_list:
        dist = []
        # arr[0] 1번째, arr[2] 2번째 ...
        for ex, ey in arr:
            d = abs(ex - x) + abs(ey - y)
            dist.append(d)

        # 정렬??
        dist.sort()

        # 임시 변수
        temp = 0
        # dist[0] 1번째 까지 포함한 거리
        # dist[1] 2번째 까지 포함한 거리...
        for i in range(len(dist)):
            d = dist[i]
            temp += d
            if ans[i] == -1 : ans[i] = temp
            else: ans[i] = min(temp, ans[i])

print(*ans)
