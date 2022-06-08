a = str(input())
# print(a)
b = []
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        # print(a[i:j])
        b.append(a[i:j])
b = set(b)
print(len(b))
