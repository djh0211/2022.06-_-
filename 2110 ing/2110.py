n,c = map(int,input().split())
xs = []
for i in range(n):
    xs.append(int(input()))
xs.sort()

start, end = 1, max(xs)
answer = 0
while(start <= end):
    mid = (start + end) // 2
    current = xs[0]
    count = 1
    for i in range(1,len(xs)):
        if xs[i] >= current + mid:
            count += 1
    if count >= c:
        start = mid+1
        answer = max(answer,mid)
    else:
        end = mid-1
print(answer)    

