def solution(n):
    INF = int(1e9)
    if n%15==0:
        return (n//5)
    else:    
        base = n//15
        a = n - base*15
        ing = INF
        for b in range(0,(a//5)+1):
            temp = a - 5*b
            if temp == 0:
                ing = min(ing, base*3 + b)
            elif temp % 3 == 0:
                ing = min(ing,base*3 + b + (temp//3))
        if ing!=INF:
            return ing
        else:
            return -1

        return -1
        
# 정확성: 26.4
# 효율성: 8.0
# 합계: 34.4 / 40.0