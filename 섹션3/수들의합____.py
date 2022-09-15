import sys
input = sys.stdin.readline

n,m= map(int,input().split())
A = list(map(int,input().split()))
subsum=A[0]
i,j=0,1 
cnt=0
while i<n:
    if subsum < m:
        if j<n:
            subsum += A[j]
            j+=1
        else:
            break
    elif subsum == m:
        cnt+=1
        subsum -= A[i]
        i+=1
    else:
        subsum -= A[i]
        i+=1

print(cnt)