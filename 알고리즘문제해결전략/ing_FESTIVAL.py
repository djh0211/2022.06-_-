
# TODO
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,L = map(int,input().split())
    pay = list(map(int,input().split()))
    dp = [0] * 1001

    if N==1:
        print(pay[0])
        continue
    else:
        dp[0] = pay[0]
        for i in range(1,N):
            dp[i]=dp[i-1]+pay[i]
        cost = dp[L-1]//L
        for n_days in range(L,N+1):
            for i in range(N-n_days+1):
                cost = max((dp[n_days-1+i] - dp[i]),cost)

            0 ~ n_days-1 ... N-1
            N-1-n_days+1+1 = N-n_days+1 번
            n_days-1 + N-n_days = N-1

        # 3, 1, 2, 3, 1, 2
        3 4 6 9 10 12
        