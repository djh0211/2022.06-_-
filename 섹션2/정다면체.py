import sys
from itertools import product
from collections import Counter

input = sys.stdin.readline

n,m = map(int, input().split())
A = list(range(1,n+1))
B = list(range(1,m+1))

cartesian = [sum(x) for x in product(A,B)]
counter = Counter(cartesian)
it = counter.most_common()
k = it[0][1]
for i in it:
    if i[1]!=k:
        break
    print(i[0],end=' ')
    

