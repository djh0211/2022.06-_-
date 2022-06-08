n,c = map(int,input().split())
xs = []
for i in range(n):
    xs.append(int(input()))
xs.sort()

start, end = 0, max(xs)

