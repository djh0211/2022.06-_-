from collections import Counter
def solution(p):
    answer = 0
    p.sort()
    result = Counter(p)
    dic= dict(result.most_common())
    
    ll = []
    
    if len(p)%2==0:
        for i in range(len(p)//2):
            it= iter(dic)
            a= next(it)
            b= next(it)
            if dic[a]!=0 and dic[b]!=0:
                dic[a] -= 1
                dic[b] -= 1
                ll.append(a)
                ll.append(b)
            dic = dict(sorted(dic.items(), key=lambda x:(-x[1], x[0])))
    else:
        if len(p)>=2:
            for i in range(len(p)//2):
                it= iter(dic)
                a= next(it)
                b= next(it)
                if dic[a]!=0 and dic[b]!=0:
                    dic[a] -= 1
                    dic[b] -= 1
                    ll.append(a)
                    ll.append(b)
                dic = dict(sorted(dic.items(), key=lambda x:(-x[1], x[0])))
            it= iter(dic)
            a= next(it)
            dic[a] -= 1
            ll.append(a)
    if len(p)>=2:
        for i in range(1,len(ll)):
            if ll[i]>ll[i-1]:
                answer+=1

    # print(len(ll))

    return answer

# 정확성: 32.5
# 효율성: 0.0
# 합계: 32.5 / 60.0