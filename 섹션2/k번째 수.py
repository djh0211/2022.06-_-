import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n,s,e,k = map(int, input().split())
    nums = list(map(int,input().split()))
    print(sorted(nums[s-1:e])[k-1])
