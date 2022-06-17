import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n,k = map(int, input().split())
dp = [INF] * (100001)
heap=[]

def dijkstra(n,k):
    if k<=n:
        print(n-k)
        return
    heapq.heappush(heap,[0,n])
    while heap:
        w,n = heapq.heappop(heap)
        for nx in [n+1,n-1,n*2]:
            if 0<=nx<=100000:
                if nx==n*2 and dp[nx]==INF:
                    dp[nx] = w
                    heapq.heappush(heap,[w,nx])
                elif dp[nx]==INF:
                    dp[nx] = w+1
                    heapq.heappush(heap,[w+1,nx])
    print(dp[k])
dijkstra(n,k)


