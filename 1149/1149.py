import sys
input = sys.stdin.readline
N = int(input())

costs = [[]for _ in range(N+1)]
for i in range(1, N+1):
    costs[i] = list(map(int,input().split()))

dp = [[0 for _ in range(3)] for _ in range(N+1)]
dp[1][0] = costs[1][0]
dp[1][1] = costs[1][1]
dp[1][2] = costs[1][2]
for k in range(2,N+1):
    dp[k][0] = min(dp[k-1][1]+costs[k][0],dp[k-1][2]+costs[k][0])
    dp[k][1] = min(dp[k-1][0]+costs[k][1],dp[k-1][2]+costs[k][1])
    dp[k][2] = min(dp[k-1][0]+costs[k][2],dp[k-1][1]+costs[k][2])
res = min(dp[N][0],dp[N][1],dp[N][2])
print(res)


'''
dp[1][0] = costs[1][0]
dp[1][1] = costs[1][1]
dp[1][2] = costs[1][2]

dp[2][0] = max(dp[1][1]+costs[2][0], dp[1][2]+costs[2][0])
dp[2][1] = max(dp[1][0]+costs[2][1], dp[1][2]+costs[2][1])
dp[2][2] = max(dp[1][0]+costs[2][2], dp[1][1]+costs[2][2])

dp[k][0] = max(dp[k-1][1]+costs[k][0],dp[k-1][2]+costs[k][0])
dp[k][1] = max(dp[k-1][0]+costs[k][1],dp[k-1][2]+costs[k][1])
dp[k][2] = max(dp[k-1][0]+costs[k][2],dp[k-1][1]+costs[k][2])
'''
