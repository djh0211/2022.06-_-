import sys
input = sys.stdin.readline
n=int(input())
a_s = list(map(int, input().split()))
x = int(input())
a_s.sort()

answer = 0
left,right = 0,n-1


while left<right:
    temp = a_s[left]+a_s[right]
    if temp == x:
        answer+=1
    elif temp > x:
        right -= 1
    else:
        left += 1
print(answer)