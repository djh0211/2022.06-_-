import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]

dp[0] = arr[0]

for k in range(1,n):
    dp[k] = max(dp[k-1]+arr[k],arr[k])

res = max(dp)
print(res)