import sys
input = sys.stdin.readline

N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int,input().split())))
lines.sort()

B = list(zip(*lines))[1]
print(B)
d = [0]*(N)
for i in range(N):
    for j in range(i):
        if B[i]>B[j] and d[i]<d[j]:
            d[i] = d[j]
    d[i] += 1

print(N - max(d))
