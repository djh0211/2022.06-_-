import sys

input = sys.stdin.readline()

N = int(input)

def solution(N):
    if(N <= 1):
        return 1
    else:
        return N * solution(N-1)

print(solution(N))