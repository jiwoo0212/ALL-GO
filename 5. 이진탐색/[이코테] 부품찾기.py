# 부품찾기
import sys
def binary_search(lst, val, start, end):
    while end >= start:
        mid = (start+end)//2
        if val == lst[mid]:
            return mid
        elif val < lst[mid]:
            end = mid-1
        elif val > lst[mid]:
            start = mid + 1
    return None

n = int(input())
n_lst = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
m_lst = list(map(int, sys.stdin.readline().rstrip().split()))

n_lst.sort()
for i in range(m):
    if binary_search(n_lst, m_lst[i], 0, n-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')