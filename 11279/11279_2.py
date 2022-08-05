import sys
import heapq

input = sys.stdin.readline
heap = []

N = int(input())

for _ in range(N):
    query = int(input())
    if query==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-query,query))





    

# heapq.heappush(heap, (-2,2))
# heapq.heappush(heap, (-4,4))
# heapq.heappush(heap, (-3,3))
# heapq.heappush(heap, (1,-1))

# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))

