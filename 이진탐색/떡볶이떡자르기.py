n,m = map(int,input().split())
cakes = list(map(int,input().split()))

start, end = 0, max(cakes)
result = 0
while(start <= end):
    mid = (start + end)//2
    total = 0
    for cake in enumerate(cakes):
        if(cake > mid):
            total += (cake-mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)



