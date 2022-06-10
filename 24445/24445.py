import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[]for i in range(n+1)]
visited = [0 for i in range(n+1)]
start = r

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)

from collections import deque

def bfs(graph,visited,start):
    queue = deque()
    queue.append(start)
    count = 1
    visited[start] = count

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                count += 1
                visited[i] = count

bfs(graph,visited,start)

for i in range(1,n+1):
    print(visited[i])



