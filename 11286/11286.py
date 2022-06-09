import sys
input = sys.stdin.readline

import heapq
n = int(input())
heap = []

for i in range(n):
    query = int(input())
    if query == 0 and not heap:
        print('0')
    elif query == 0 and heap:
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(query), query))

# -2 -4 4 2 3 -> -2 2 3 -4 4
