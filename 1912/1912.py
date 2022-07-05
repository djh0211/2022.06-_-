import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
'''
10 -4 3 1 5 6 -35 12 21 -1
0행은 해당 인덱스의 수를 포함하지 않을때
1행은 해당 인덱스의 수를 포함할때
dp[0][0] = 0
dp[1][0] = dp[0][0] + 10
dp[0][1] = max(dp[0][0], dp[1][0])
dp[1][1] = dp[0][1] + (-4)
...
res = max(dp[0][n-1], dp[1][n-1])
'''

dp[0] = arr[0]

for k in range(1,n):
    dp[k] = max(dp[k-1]+arr[k],arr[k])

res = max(dp)
print(res)