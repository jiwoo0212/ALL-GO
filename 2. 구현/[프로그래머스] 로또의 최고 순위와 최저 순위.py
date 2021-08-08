def solution(lottos, win_nums):
    
    lst = [6, 6, 5, 4, 3, 2, 1]
    
    cnt1 = 0
    cnt2 = 0
    
    for i in lottos:
        if i in win_nums:
            cnt1 += 1
        if i == 0:
            cnt2 += 1
    
    low_result = lst[cnt1]
    up_result = lst[cnt1+cnt2]
    
    return [up_result, low_result]