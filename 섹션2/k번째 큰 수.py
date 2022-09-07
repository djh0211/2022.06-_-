import sys
from itertools import combinations
input = sys.stdin.readline

n,k = map(int, input().split())
cards = list(map(int, input().split()))

print(sorted(list(set(list(sum(x) for x in combinations(cards,3)))),reverse=True)[k-1])