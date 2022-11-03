import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        name, drinks = input().rstrip().split()
        lst.append((name, int(drinks)))
    lst.sort(key=lambda x:x[1])
    print(lst[-1][0])