import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr=list(map(int,input().split()))

part_sum = sum(arr[:k])
max_sum = part_sum

for i in range(n-k):
    part_sum = part_sum - arr[i] + arr[i+k]
    max_sum = max(part_sum,max_sum)

print(max_sum)

'''
0을빼고 k+1을 담아
1     k+2
...
n-k-2 n-1
'''