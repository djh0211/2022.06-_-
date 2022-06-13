import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    a = list(input())[:-1]
    graph.append(list(map(int,a)))
visited =[[0 for _ in range(m)] for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(graph,visited,sx,sy):
    global n
    global m
    queue = deque()
    queue.append((sx,sy))
    visited[sx][sy] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny= x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1 and visited[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1


bfs(graph,visited,0,0)

print(visited[n-1][m-1])
