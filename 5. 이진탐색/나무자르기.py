def binary_search(val, start, end):
    while start <= end:
        mid = (start + end)//2
        mid_val = sum([logs[i] - mid for i in range(len(logs)) if logs[i]>=mid])

        if mid_val == val:
            return mid
        elif mid_val < val:
            end = mid - 1
        elif mid_val > val:
            result = mid
            start = mid + 1
    return result

import sys
n, m = map(int, input().split())
logs = list(map(int, sys.stdin.readline().rstrip().split()))
print(binary_search(m, 0, max(logs)-1))