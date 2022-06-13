import sys
from collections import deque

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

input = sys.stdin.readline
m,n,h = map(int,input().split())
graph = [[[]for i in range(n)] for j in range(h)]
# print(graph)
for i in range(h):
    for j in range(n):
        graph[i][j]=list(map(int,input().split()))

visited = [[[False for i in range(m)] for j in range(n)]for k in range(h)]
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

def bfs(graph,visited,queue):
    while queue:
        x,y,z = queue.popleft()
        visited[x][y][z]=True
        for i in range(6):
            nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
            if 0<=nx< h and 0 <= ny < n and 0<=nz<m and graph[nx][ny][nz]==0 and visited[nx][ny][nz] == False:
                queue.append((nx,ny,nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1

bfs(graph,visited,queue)
res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
        res = max(max(graph[i][j]),res)
print(res-1)
            
