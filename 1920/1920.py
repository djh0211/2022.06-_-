import bisect
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

A.sort()

for b in B:
    left = bisect.bisect_left(A,b)
    status = False
    if left < len(A):
        if A[left] == b:
            status = True
    
    if status:
        print('1')
    else:
        print('0')

    # right = bisect.bisect_right(A,b)

