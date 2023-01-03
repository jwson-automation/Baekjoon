N = int(input())
cards = list(map(int, input().split()))
cards.sort()
cardsDic = {}

for c in cards:
    if c not in cardsDic:
        cardsDic[c] = 1
    else:
        cardsDic[c] += 1

M = int(input())
nums = list(map(int, input().split()))


for n in nums:
    start = 0
    end = N-1

    while start <= end:
        mid = (start+end)//2

        if cards[mid] == n:
            break

        if cards[mid] > n:
            end = mid - 1

        if cards[mid] < n:
            start = mid + 1

    if cards[mid] == n:
        print(cardsDic[n], end=" ")
    else:
        print(0, end=" ")