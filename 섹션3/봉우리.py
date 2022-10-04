import sys
input = sys.stdin.readline

n=int(input())
board = [[0 for _ in range(n+2)]for _ in range(n+2)]
for i in range(1,n+1):
    board[i][1:-1] = list(map(int,input().split()))
    
# print(board)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        target = board[i][j]
        flag = True
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            cons = board[nx][ny]
            if target<=cons:
                flag = False
        if flag:
            cnt+=1

print(cnt)            

# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2