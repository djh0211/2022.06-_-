import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())

def get_prime(n):
    a = [True] * (n+1)
    for i in range(2,int(sqrt(n))+1):
        if a[i] == True:
            j=2
            while i*j<=n:
                a[i*j] = False
                j += 1
            
    return len([i for i in range(2,n+1) if a[i]==True])



print(get_prime(n))