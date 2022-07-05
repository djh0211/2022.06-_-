
# TODO: 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
import sys
input = sys.stdin.readline
T = int(input())
Ns = []
for _ in range(T):
    Ns.append(int(input()))
max_N = max(Ns)

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for k in range(4,max_N+1):
    dp[k] = dp[k-3]+dp[k-2]
for n in Ns:
    print(dp[n])




