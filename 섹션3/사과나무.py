import sys
input = sys.stdin.readline

n = int(input())
board = [[]for _ in range(n)]
for i in range(n):
    board[i] = list(map(int,input().split()))

s = e = n//2
goal = 0
for i in range(n):
    for j in range(s,e+1):
        goal += board[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(goal)