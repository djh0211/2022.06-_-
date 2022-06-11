import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

def dfs(graph,visited,start):
    global count
    count += 1
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph,visited,i)

dfs(graph,visited,1)
print(count-1)

