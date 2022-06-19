while(True):
    a, b = list(map(int, input().split()))
    
    # 0, 0
    if(a + b == 0):
        break
    
    # case 1
    if(a < b):
        if(b % a == 0):
            print('factor')
        else:
            print('neither')
    elif(a > b):
        if(a % b == 0):
            print('multiple')
        else:
            print('neither')