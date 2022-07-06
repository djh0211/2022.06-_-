import sys
input = sys.stdin.readline
N = int(input())

dp = [0] * (int(1e6)+1)
dp[2] = 1
dp[3] = 1

for k in range(4,N+1):
    tmp = []
    if k%3 ==0:
        tmp.append(dp[k//3]+1)
    if k%2 == 0:
        tmp.append(dp[k//2]+1)
    tmp.append(dp[k-1]+1)
    dp[k] = min(tmp)
print(dp[N])




        




# dp[4] = 