import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
people = [[]for _ in range(n)]

def counting(l : list):
    s = set(l)
    counter = Counter(l)
    if len(s)==1:
        return (10000 + l[0]*1000)
    elif len(s)==2:
        return(1000 + 100*counter.most_common()[0][0])
    else:
        return(100*max(l))

for i in range(n):
    temp = list(map(int, input().split()))
    people[i].append(counting(temp))

print(max(people)[0])



    



