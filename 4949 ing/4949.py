import re
while(1):
    try:
        a = str(input())
        b = re.sub(r'[^[\]\(\)]','',a)

        stack = []

        for i in b:
            if i == '[' or i == '(':
                stack.append(i)
            elif i == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            elif i == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        else:
            if stack:
                print('no')
            else:
                print('yes')
    except EOFError as e:
        break