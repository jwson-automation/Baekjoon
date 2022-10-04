import sys

l, c = map(int,input().split())

letters = list(map(str, input().split()))

letters.sort()

visited = [0 for _ in range (c+1)]

def check(string):
    count = 0
    for alpha in string:
        if alpha == 'a' or alpha == 'i' or alpha == 'u' or alpha == 'e' or alpha == 'o':
            count += 1
    return count

# 콤비네이션 사용시 아래처럼 
# for case in combinations(alphabet, L):
#     if check(case) >= 1 and (len(case) - check(case)) >= 2:
#         print(''.join(case))

def dfs (depth, string, index):
    if depth == l:
        if check(string) >= 1 and (len(string) - check(string)) >= 2 :
            print(''.join(string))
            return
    
    for i in range(c):
        if index < i:
            if not visited[i]:
                visited[i] = 1
                string.append(letters[i])
                dfs(depth+1, string, i)
                visited[i] = 0
                string.pop()

dfs(0,[],-1)

# 최소 한개의 모음 ( a,i,u,e,o) + 최소 2개의 자음

