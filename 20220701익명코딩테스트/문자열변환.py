def solution(s):
    # Write your code here
    max_b = sorted(list(s))[::-1]
    # print(max_b)
    res = []
    # print(5//2)
    # print(4//2)
    if len(max_b)%2==0:
        for i in range((len(max_b)//2)):
            # print(i)
            if i == len(max_b)-1-i:
                res.append(max_b[i])
            else:
                res.append(max_b[i])
                res.append(max_b[len(max_b)-1-i])
    else:
        for i in range((len(max_b)//2)+1):
            # print(i)
            if i == len(max_b)-1-i:
                res.append(max_b[i])
            else:
                res.append(max_b[i])
                res.append(max_b[len(max_b)-1-i])
        
                
    return ''.join(res[::-1])