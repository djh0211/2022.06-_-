import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

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

count = 1

def dfs(graph,visited,v):
    global count
    visited[v] = count
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(graph,visited,i)

dfs(graph,visited,start)

for i in range(1,n+1):
    print(visited[i])