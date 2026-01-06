from collections import defaultdict
from typing import List
class solution:
    def maxLength(nums):
        n = len(nums)
        l = [0]*(n+1)
        count0 =0 
        count1 =0 
        for i in range(len(nums)):
            if nums[i] ==0:
                count0+=1
            else:
                count1+=1
            diff = count0-count1
            l[i+1] = diff
        d = {}
        best = 0
        for idx,x in enumerate(l):
            if x not in d:
                d[x] = idx
            else:
                best = max(best, idx-d[x]+1)
        return best


