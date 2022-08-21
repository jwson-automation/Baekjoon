import sys
input = sys.stdin.readline

min_a = min_b = min_c = 0
max_a = max_b = max_c = 0

n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())

    min_a, min_b, min_c = (min(min_a, min_b) + a, 
                          min(min_a, min_b, min_c) + b, 
                          min(min_b, min_c) + c)

    max_a, max_b, max_c = (max(max_a, max_b) + a, 
                          max(max_a, max_b, max_c) + b, 
                          max(max_b, max_c) + c)   

print(max(max_a, max_b, max_c), min(min_a, min_b, min_c)) 