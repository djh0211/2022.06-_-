import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

res = []

def digit_sum(x):
    # print(x)
    return sum(list(map(int,list(str(x)))))

for num in nums:
    res.append(digit_sum(num))
    # digit_sum(num)
    # print(digit_sum(num))

idx = -1111
MAX = -1111 
for i, num in enumerate(res):
    if MAX < num:
        MAX = num
        idx = i
    
print(nums[idx])
