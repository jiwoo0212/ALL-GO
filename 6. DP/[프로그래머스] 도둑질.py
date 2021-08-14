def solution(money):
    result = -1
    for case in range(2): # case1: 첫번째 o, 마지막 x, case2: 첫번째 x
        d = [0 for _ in range(len(money))]
        if case == 1:
            d[0] = money[0]
        d[1] = max(d[0], money[1])
        for i in range(2, len(d)):
            if case==1 and i==(len(d)-1): # 첫번째 o, 마지막 x
                d[i] = d[i-1]
            else:
                d[i] = max(money[i]+d[i-2], d[i-1]) 
        if d[-1] > result:
            result = d[-1]
    return result