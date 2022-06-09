import sys
input = sys.stdin.readline
n= int(input())
import heapq
heap = []

for i in range(n):
    query = int(input())
    if query == 0 and not heap:
        print('0')
    elif query == 0 and heap:
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-query,query))

