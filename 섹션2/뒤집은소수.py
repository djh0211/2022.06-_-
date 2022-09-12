import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    a = [True]*(x+1)
    a[1] = False
    for i in range(2,int(sqrt(x))+1):
        if a[i] == True:
            j=2
            while i*j <= x:
                a[i*j] = False
                j+=1
    if a[x]==True:
        print(x,end=' ')
    

for num in nums:
    isPrime(reverse(num))
