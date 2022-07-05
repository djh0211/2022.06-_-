import sys
input = sys.stdin.readline

N = int(input())
pyramid = []
for i in range(N):
    pyramid.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(len(pyramid[i])):
        if j==0:
            pyramid[i][j] += pyramid[i-1][j]
        elif j==i:
            pyramid[i][j] += pyramid[i-1][-1]
        else:
            pyramid[i][j] += max(pyramid[i-1][j],pyramid[i-1][j-1])

print(max(pyramid[-1]))
