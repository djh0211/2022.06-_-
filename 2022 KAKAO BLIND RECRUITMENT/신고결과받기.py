def solution(id_list, report, k):
    answer = []
    dic = {}
    # dic['a'] = [1,['b','c']]
    # print(dic)
    
    for r in report:
        a,b = map(str,r.split())
        # 신고당한적없으면
        if b not in dic:
            dic[b] = [1,[a]]
        # 중복신고 아니면
        elif a not in dic[b][1]:
            dic[b][0] += 1
            dic[b][1].append(a)

            
    ss = {}
    for i in id_list:
        ss[i] = 0
    
    for row in dic.items():
        # 일정이상 신고
        if row[1][0]>=k:
            for i in row[1][1]:
                ss[i] += 1
    
    for i in ss.values():
        answer.append(i)
            
    return answer