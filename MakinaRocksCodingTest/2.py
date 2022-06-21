def solution(price):
    mid = sorted(price)[len(price)//2]
    
    answer = []

    for p_idx,pivot in enumerate(price):
        first = -1

        if mid >= pivot:
            for i in range(p_idx+1,len(price)):
                if price[i]>pivot:
                    first = i - p_idx
                    answer.append(first)
                    break
        else:
            ss = price[p_idx:]
            ss.sort()
            if ss.index(pivot) < len(ss)-1:
                for i in range(p_idx+1,len(price)):
                    if price[i]>pivot:
                        first = i - p_idx
                        answer.append(first)
                        break
        if first==-1:
            answer.append(first)


    return answer

# 정확성: 42.0
# 효율성: 0.0
# 합계: 42.0 / 60.0