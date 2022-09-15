import sys
input = sys.stdin.readline

n=int(input())
arr1 = list(map(int, input().split()))
m=int(input())
arr2 = list(map(int, input().split()))

ll = []
c1,c2=0,0
while 1:
    if c1 == n and c2==m:
        break
    elif c1 == n:
        ll += arr2[c2:]
        break
    elif c2 == m:
        ll += arr1[c1:]
        break
    else:
        if arr1[c1] >= arr2[c2]:
            ll.append(arr2[c2])
            c2+=1
        else:
            ll.append(arr1[c1])
            c1+=1
print(ll)