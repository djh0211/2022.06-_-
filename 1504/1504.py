import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s1,s2 = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

route1 = []
route2 = []

dijkstra(1)
if distance[s1] != INF:
    route1.append(distance[s1])
else:
    route1.append('INF')

if distance[s2] != INF:
    route2.append(distance[s2])
else:
    route2.append('INF')

distance = [INF] * (n+1)
dijkstra(s1)
if distance[s2] != INF:
    route1.append(distance[s2])
else:
    route1.append('INF')
if distance[n] != INF:
    route2.append(distance[n])
else:
    route2.append('INF')

distance = [INF] * (n+1)
dijkstra(s2)
if distance[s1] != INF:
    route2.append(distance[s1])
else:
    route2.append('INF')
if distance[n] != INF:
    route1.append(distance[n])
else:
    route1.append('INF')

if 'INF' in route1 and 'INF' in route2:
    print(-1)
elif 'INF' in route1 and 'INF' not in route2:
    print(sum(route2))
elif 'INF' not in route1 and 'INF' in route2:
    print(sum(route1))
else:
    print(min(sum(route1),sum(route2)))