import sys

input = sys.stdin.readline
N=int(input())
mine = set(list(map(int, input().split())))
M=int(input())
cards = list(map(int, input().split()))

for card in cards:
    if card in mine:
        print(1,end=' ')
    else:
        print(0,end=' ')



