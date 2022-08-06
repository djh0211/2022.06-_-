import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n,e = map(int, input().split())
graph = [[]for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(start,distance):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

route1=[]
route2=[]

# 1->v1->v2->N
# 1->v2->v1->N

dijkstra(1,distance)
route1.append(distance[v1]) # 1->v1
route2.append(distance[v2]) # 1->v2

distance = [INF] * (n+1)
dijkstra(v1,distance)
route1.append(distance[v2]) # v1->v2
route2.append(distance[n]) # v1->N

distance = [INF] * (n+1)
dijkstra(v2,distance)
route1.append(distance[n]) # v2->N
route2.append(distance[v1]) # v2->V1

if INF in route1 and INF in route2:
    print(-1)
elif INF in route1:
    print(sum(route2))
elif INF in route2:
    print(sum(route1))
else:
    print(min(sum(route1),sum(route2)))

