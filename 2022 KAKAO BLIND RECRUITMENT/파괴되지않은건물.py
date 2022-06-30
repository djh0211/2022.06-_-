def solution(board, skill):
    answer = 0
    for turn in skill:
        # 공격
        degree = turn[-1]
        if turn[0]==1:
            degree = -degree
        sx,sy = min(turn[1],turn[3]),min(turn[2],turn[4])
        ex,ey = max(turn[1],turn[3]),max(turn[2],turn[4])
        dx,dy = ex-sx+1,ey-sy+1
        
        for row in board[sx:ex+1]:
            row[sy:ey+1] = [i+j for i,j in zip(row[sy:ey+1],[degree]*dy)]
        # print(board)
    
    for i in board:
        for j in i:
            if j>0:
                answer+=1
    
            
        
        




#     a = [[0 for _ in range(4)]for _ in range(5)]
#     for row in a[1:-1]:
        
#         row[1:-1] = [i+j for i,j in zip(row[1:-1],[-1]*2)]
#     print(a)
    
        
            
            
    return answer