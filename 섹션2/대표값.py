import sys
from bisect import bisect_left

input = sys.stdin.readline
inf = int(1e9)
n = int(input())
numbers = list(map(int, input().split()))
# numbers.sort()
mean = round(sum(numbers)/n)
min_gap = inf
idx = 0

for i in range(n):
    if abs(mean - numbers[i]) < min_gap:
        min_gap = abs(mean - numbers[i])
        idx = i
    elif abs(mean - numbers[i]) == min_gap:
        if numbers[i] > numbers[idx]:
            idx = i

print(mean,idx+1,sep=' ')

    


# idx = bisect_left(numbers, mean)
