import sys

input = sys.stdin.readline()

N = int(input)

def solution(N):
    global map
    if(N==3):
        map[0][:3] = map[2][:3] = [1]*3
        map[1] = [1,0,1]
        return
    a = N//3
    solution(a)
    for i in range(3):
        for j in range(3):
            if(i==1 & j==1):
                continue
            map[]
        
