n,m = map(int,input().split())
s = []
candidates=[]
for i in range(n):
    s.append(str(input()))
for i in range(m):
    candidates.append(str(input()))
s = set(s)

cnt = 0
for i in candidates:
    if i in s:
        cnt+=1
print(cnt)

