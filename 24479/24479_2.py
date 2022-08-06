import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M,R = map(int,input().split())
graph=[[]for _ in range(N+1)]
visited = [0] * (N+1)
count = 1

for _ in range(M):
    u,v= map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    global count
    visited[v] = count
    graph[v].sort()
    
    for g in graph[v]:
        if visited[g] == 0:
            count+=1
            dfs(g)


dfs(R)

for i in range(1, N + 1):
    print(visited[i])

