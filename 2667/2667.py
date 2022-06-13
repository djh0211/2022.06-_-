import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = []
for i in range(n):
    a = list(input())[:-1]
    graph.append(list(map(int,a)))

visited = [[False for _ in range(n)] for _ in range(n)]

eachcount = 0
results = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(graph,visited,x,y):
    global eachcount
    visited[x][y] = True
    eachcount += 1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<len(graph) and 0<=ny<len(graph) and visited[nx][ny] == False and graph[nx][ny] == 1:
            dfs(graph,visited,nx,ny)

for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==False:
            dfs(graph,visited,i,j)
            results.append(eachcount)
            eachcount = 0

print(len(results))
results.sort()
for i in results:
    print(i)


