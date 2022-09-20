import sys
input = sys.stdin.readline

n = int(input())
board = [[]for i in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))
# print(board)

def sol(n):
    max_sum = -999
    for i in range(n):
        max_sum = max(sum(board[i]), max_sum)
    temp = [0]*n
    for i in range(n):
        temp = [sum(a) for a in zip(board[i],temp)]
    # print(max(temp))
    max_sum = max(max(temp),max_sum)
    temp=0
    for i in range(n):
        temp += board[i][i]
    max_sum = max(max_sum,temp)

    print(max_sum)

sol(n)