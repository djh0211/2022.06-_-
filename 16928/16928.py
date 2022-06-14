import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())

ladders={}
snakes={}

for i in range(n):
    u,v = map(int,input().split())
    ladders[u] = v

for i in range(m):
    u,v = map(int,input().split())
    snakes[u] = v

visited = [0]*101

def bfs(ladders,snakes,visited):
    queue = deque()
    queue.append(1)
    while queue:
        x = queue.popleft()
        if x == 100:
            return visited[x]
        for i in range(1,7):
            nx = x+i
            if 1<=nx<=100 and visited[nx]==0:
                if nx in ladders:
                    queue.append(ladders[nx])
                    if visited[nx]!=0:
                        visited[nx] = min(visited[nx],visited[x]+1)
                    elif visited[ladders[nx]]!=0:
                        visited[ladders[nx]] = min(visited[ladders[nx]],visited[x]+1)
                    else:
                        visited[nx] = visited[x]+1
                        visited[ladders[nx]] = visited[x]+1
                elif nx in snakes:
                    queue.append(snakes[nx])
                    if visited[nx]!=0:
                        visited[nx] = min(visited[nx],visited[x]+1)
                    elif visited[snakes[nx]]!=0:
                        visited[snakes[nx]] = min(visited[snakes[nx]],visited[x]+1)
                    else:
                        visited[nx] = visited[x]+1
                        visited[snakes[nx]] = visited[x]+1
                else:
                    queue.append(nx)
                    if visited[nx]!=0:
                        visited[nx] = min(visited[nx],visited[x]+1)
                    else:
                        visited[nx] = visited[x]+1

print(bfs(ladders,snakes,visited))
