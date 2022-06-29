def solution(fees, records):
    answer = []
    import datetime
    basic=fees[:2]
    over=fees[2:]
    dic = {}
    
    for record in records:
        # 새로운 차 기록이면
        if record.split()[1] not in dic:
            dic[record.split()[1]] = [record.split()[0]]
        else:
            dic[record.split()[1]].append(record.split()[0])
    ll={}
    
    def divide_list(l, n): 
        # 리스트 l의 길이가 n이면 계속 반복
        for i in range(0, len(l), n): 
            yield l[i:i + n] 
            
    for row in dic.items():
        num = row[0]
        record = row[1]
        temp=0
        for couple in iter(list(divide_list(record, 2))):
            # 출차가 안됨
            if len(couple)!=2:
                a = datetime.datetime.strptime(couple[0],"%H:%M")
                b = datetime.datetime.strptime("23:59","%H:%M")
                c = str(b-a).split(':')[:-1]
            else:  
                a = datetime.datetime.strptime(couple[0],"%H:%M")
                b = datetime.datetime.strptime(couple[1],"%H:%M")
                c = str(b-a).split(':')[:-1]
            d = int(c[0])*60+int(c[1])
            temp += d
        
        if temp <= basic[0]:
            ll[int(num)] = basic[1]
        # 기본요금 초과
        elif temp>=basic[0]:
        # 올림해야함
            if (temp-basic[0])%over[0] != 0:
                ll[int(num)] = basic[1] + (((temp-basic[0])//over[0])+1)*over[1]
            else:
                ll[int(num)] = basic[1] + ((temp-basic[0])//over[0])*over[1]
    for i in sorted(ll.items()):
        answer.append(i[1])

    return answer