import sys
input = sys.stdin.readline

n = int(input())
board = [[]for i in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

def sol(q,n):
    a,b,c = q
    a -= 1
    c = c % n
    # TODO 왼쪽으로 회전
    if b==0:
        board[a] = board[a][c:]+board[a][:c]
    # TODO 오른쪽으로 회전
    else:
        board[a] = board[a][-c:]+board[a][:-c]
        
m= int(input())
for i in range(m):
    q = list(map(int, input().split()))
    sol(q,n)

s,e= 0,n-1
res=0

for i in range(n):
    for j in range(s,e+1):
        res += board[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)