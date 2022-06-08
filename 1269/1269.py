n,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = set(A)
B = set(B)

C = A.intersection(B)
# print(C)
D = A-C
E = B-C
print(len(D)+len(E))