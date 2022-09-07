import sys
from math import sqrt


input = sys.stdin.readline

n,k = map(int,input().split())
# print(n,k)

nums = []

for i in range(1,n+1):
    if n%i == 0:
        nums.append(i)
    else:
        continue

if len(nums)<k:
    print(-1)
else:
    print(nums[k-1])



