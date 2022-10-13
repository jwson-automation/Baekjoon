import sys
input = sys.stdin.readline

n = int(input())
answer_sheet = set(map(int,input().split()))

m = int(input())
tmp_numbers = list(map(int,input().split()))

for k in tmp_numbers:
    if k in answer_sheet: print(1)
    else: print(0)