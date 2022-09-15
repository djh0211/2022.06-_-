import sys
input = sys.stdin.readline
import re

# word = str(input())
word = 'g0en2Ts8eSoft'
x = int(re.sub('[^0-9]','', word))
print(x)
cnt=0
for i in range(1,x+1):
    if x % i == 0:
        cnt+=1
print(cnt)
