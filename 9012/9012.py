n = int(input())
flags=[]
for i in range(n):
    stack = []
    a = str(input())
    flag = True
    for j in a:
        if j == '(':
            stack.append(j)
        else:
            if len(stack):
                stack.pop()

            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
