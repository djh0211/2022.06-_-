import sys
from collections import deque
input = sys.stdin.readline

dx = [2,1,-1,-2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]


def bfs(l,n,m,visited):
    queue = deque()
    queue.append(n)
    while queue:
        x,y = queue.popleft()
        if (x,y)==m:
            return visited[x][y]
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==False:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1






res = []
t = int(input())
for i in range(t):
    l = int(input())
    visited = [[0 for _ in range(l)] for _ in range(l)]
    a, b = map(int,input().split())
    n = (a,b)
    a, b = map(int,input().split())
    m = (a,b)

    res.append(bfs(l,n,m,visited))

for i in res:
    print(i)


# 1
# 8
# 0 0
# 7 0