house = int(input())
location = list(map(int,input().split()))
location.sort(reverse=True)

answer = location[house//2]

print(answer)