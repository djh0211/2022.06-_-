import sys

input = sys.stdin.readline

K,N = map(int, input().split())
lans = []
for _ in range(K):
    lans.append(int(input()))

start,end = 1,max(lans)

while end>=start:
    num = 0
    mid= (start + end) // 2

    for lan in lans:
        num += lan//mid
    
    if num >= N:
        start = mid+1
    else:
        end = mid-1

print(end)

# 1 802 401
# 1 400 200
# 201 400 300
# 201 299 250
# 201 249 225
# 201 224 212
# 201 211 206
# 201 205 203
# 201 202 201
# 201 200 end
