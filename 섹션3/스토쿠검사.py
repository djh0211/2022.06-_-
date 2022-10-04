import sys
input = sys.stdin.readline

board = [[]for _ in range(9)]

comparison = set(list(range(1,10)))

for i in range(9):
    board[i] = list(map(int,input().split()))
    if set(board[i])!=comparison:
        print("NO")
        exit()

for i in zip(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]):
    if comparison != set(i):
        print("NO")
        exit()

for i in range(3):
    for j in range(3):
        # print("\n")
        temp = board[i*3][j*3:j*3+3] + board[i*3+1][j*3:j*3+3] + board[i*3+2][j*3:j*3+3]
        if set(temp)!= comparison:
            print("NO")
            exit()
        

print("YES")
        
        
# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7