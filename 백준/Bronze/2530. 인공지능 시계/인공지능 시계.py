hour, min, sec = map(int, input().split())
plus = int(input())

S = sec+plus
M = min
H = hour

if S >= 60:
    plusM = S//60
    S1 = S-(60*plusM)
    M = min+plusM

    if M >= 60:
        plusH = M//60
        M1 = M-(60*plusH)
        H = hour+plusH

        if H >= 24:
           Hcontrol = H//24
           H1 = H-24*Hcontrol
           print(H1,M1,S1)
        else:
            print(H,M1,S1)

    else:
        print(H,M,S1)

else:
    print(H,M,S)