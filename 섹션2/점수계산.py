import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int,input().split()))
dp = [0]*(105)

dp[0] = score[0]
for i in range(1,n):
    if score[i]==0:
        dp[i]=0
    else:
        if dp[i-1]==0:
            dp[i]=1
        else:
            dp[i] = dp[i-1] + 1

print(sum(dp))

