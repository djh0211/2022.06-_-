N,K = map(int,input().split())
day = list(map(int,input().split()))
sum = sum(day[0:K])
MAX = sum
for i in range(N-K):
    sum -= (day[i]-day[i+K])
    MAX = max(MAX,sum)
print(MAX)