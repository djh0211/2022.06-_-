import sys
input = sys.stdin.readline
cards = list(range(21))
# print(cards)
for i in range(10):
    x,y = map(int, input().split())
    cards[x:y+1] = cards[x:y+1][::-1]
print(cards[1:])

# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20