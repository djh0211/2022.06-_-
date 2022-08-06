import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [2,1,-1,-2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(l,visited,now,to):
    queue = deque()
    queue.append(now)
    while queue:
        x,y = queue.popleft()
        if [x,y] == to:
            return visited[x][y]
        for i in range(8):
            nx,ny= x+dx[i],y+dy[i]
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==0:
                queue.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1



for _ in range(t):
    l = int(input())
    visited = [[0 for _ in range(l)] for _ in range(l)]

    now = list(map(int, input().split()))
    to = list(map(int, input().split()))

    print(bfs(l,visited,now,to))

    