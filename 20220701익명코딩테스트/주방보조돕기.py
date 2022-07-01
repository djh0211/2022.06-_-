def solution(ingredients, startIndex, target):
    # Write your code here
    INF = int(1e9)
    i_list = []
    for idx,i in enumerate(ingredients):
        if i==target:
            i_list.append(idx)
    # print(i_list)
    min_gap = INF
    for idx in i_list:
        a = abs(startIndex-idx)
        b = len(ingredients) - a
        temp = min(a,b)
        min_gap = min(min_gap,temp)
        
    return min_gap