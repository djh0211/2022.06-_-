import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(graph,visited,x,y):
    global m # 열
    global n # 행
    visited[x][y] = True
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=ny<m and 0<=nx<n and graph[nx][ny]==1 and visited[nx][ny]==False:
            dfs(graph,visited,nx,ny)

t = int(input())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(t):
    count = 0
    m,n,k = map(int,input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for j in range(k):
        y,x = map(int,input().split())
        graph[x][y] = 1
    for j in range(n):
        for k in range(m):
            if graph[j][k]==1 and visited[j][k]==False:
                dfs(graph,visited,j,k)
                count+=1
    print(count)

# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5
    
