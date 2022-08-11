hour, min = map(int, input().split())
cook = int(input())

T = min+cook
T1 = 0
if T >= 60:
    howHour = T//60
    T1 = T-(60*howHour)
    H1 = hour+howHour

elif T < 60:
    T1 = T
    H1 = hour

if H1 >= 24:
    H1 = H1-24
    print(H1,T1)
else:
    print(H1,T1)