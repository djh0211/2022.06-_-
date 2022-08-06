import sys
input = sys.stdin.readline

N = int(input())
points = []
for i in range(N):
    points.append(int(input()))
dp = [0] * (301)
if N == 1:
    print(points[0])
    exit()
elif N==2:
    print(points[0]+points[1])
    exit()
elif N==3:
    print(max(points[0]+points[2],points[1]+points[2]))
    exit()
else:
    dp[0] = points[0]
    dp[1] = points[0]+points[1]
    dp[2] = max(points[0]+points[2],points[1]+points[2])
    for k in range(3,N):
        dp[k] = max(dp[k-2]+points[k],dp[k-3]+points[k-1]+points[k])

    print(dp[N-1])

