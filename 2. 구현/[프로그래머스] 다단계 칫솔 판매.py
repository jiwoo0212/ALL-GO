def solution(enroll, referral, seller, amount):
    tree = {'-':'-'}
    price = {'-':0}
    
    for c, p in zip(enroll, referral):
        tree[c] = p
        price[c] = 0
    
    for i, val in zip(seller, amount):
        parent = tree[i]
        child = i
        val *= 100
        price[i] += val - int(val*0.1)
        price[parent] += int(val*0.1)

        val = int(val*0.1)
        while parent != '-':
            child = parent
            parent = tree[parent]
            price[child] -= int(val*0.1)
            price[parent] += int(val*0.1)
            if int(val*0.1) ==0:
                break
            val = int(val*0.1)
            
    answer = list(price.values())[1:]
    return answer