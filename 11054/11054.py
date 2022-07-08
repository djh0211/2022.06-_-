import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
idp = [0]*(N)
ddp = [0]*(N)

for i in range(N):
    for j in range(i):
        if A[i]>A[j] and idp[i]<idp[j]:
            idp[i] = idp[j]
    idp[i] += 1

reverseA = A[::-1]
for i in range(N):
    for j in range(i):
        if reverseA[i]>reverseA[j] and ddp[i]<ddp[j]:
            ddp[i] = ddp[j]
    ddp[i] += 1
ddp = ddp[::-1]
dp = [pair[0]+pair[1] for pair in zip(idp,ddp)]
# print(idp)
# print(ddp)
print(max(dp)-1)