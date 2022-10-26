import sys

n = int(input())
# n = 100
a = [300, 60, 10]

if n < 10: 
    print(-1)
    sys.exit()

sol = []
for i in range(3):
  if n >= a[i]:
    mok, mod = n // a[i], n%a[i]
    sol.append(mok)
    n = n - mok*a[i]
  else: 
    sol.append(0)
    
if mod == 0:
  print(*sol)
else:
  print(-1)