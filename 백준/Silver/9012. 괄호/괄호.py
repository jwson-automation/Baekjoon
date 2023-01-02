t = int(input())

for i in range(t):
    score = 0
    array = list(map(str, input().rstrip()))
    for d in range (0, len(array)):
        if array[d] == "(" :
            score += 1
        if array[d] == ")" :
            score -= 1
        if score < 0 :
            print("NO")
            break
        if d == len(array)-1 and score != 0 :
            print("NO")
            break
        if d == len(array)-1 and score == 0 :
            print("YES")
            break
