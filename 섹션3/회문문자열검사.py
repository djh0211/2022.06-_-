import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    word = str(input()).lower()[:-1]
    if word == word[::-1]:
        print('YES')
    else:
        print('NO')
    