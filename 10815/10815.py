n = int(input())
cards = list(map(int,input().split()))
m = int(input())
candidates = list(map(int,input().split()))

cards = set(cards)
result = []
for i in candidates:
    if i in cards:
        result.append(str(1))
    else:
        result.append(str(0))
print(' '.join(result))
