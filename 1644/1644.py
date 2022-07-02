import sys
import math
input = sys.stdin.readline
N = int(input())

def Primes(N):
    arr = [True] * (N+1)
    arr[0],arr[1] = False,False
    for i in range(2,int(math.sqrt(N)+1)):
        if arr[i] == True:
            j = 2
            while i*j <= N:
                arr[i*j] = False
                j += 1
    primes = []
    for idx, i in enumerate(arr):
        if i == True:
            primes.append(idx)
    return primes


if N == 1:
    print('0')
    exit()

primes = Primes(N)

left,right = 0,0
s= primes[0]
ans = 0
while True:
    if s==N:
        ans += 1
        s -= primes[left]
        left += 1
    elif s<N:
        right += 1
        if right == len(primes):
            break
        s += primes[right]
    elif s>N:
        s -= primes[left]
        left += 1

print(ans)




    
        


