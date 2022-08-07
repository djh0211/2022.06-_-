import sys
import math

input = sys.stdin.readline
N = int(input())

def GetPrimeEratosthenes(n):
    chk = [True]*(n+1)
    res = []
    chk[0], chk[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if chk[i]:
            res.append(i)
            j = 2
            while i*j <= n:
                chk[i*j] = False
                j += 1
    res = [x for x in range(n+1) if chk[x]]
    return res

primes = GetPrimeEratosthenes(N)

cnt=0
left,right=0,0
s=primes[0]
while True:
    if s==N:
        cnt+=1
    elif s<N:
        right+=1
        if right == len(primes):
            break
        s+=primes[right]
    elif s>N:
        left += 1
        s-=primes[left]

print(cnt)

