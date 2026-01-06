# fruits into basket

"""
Docstring for Day2.L904
similar problem longest window with atmost 2 distinct element. 
"""

# variable sliding window length.. start pointer moves based on the conditions.  [l,r] --> if window invalid move left pointer till window is valid.
class solution:
    def totalFruits(self,nums):
        start = 0
        best = 0
        distinct = {}
        for end in range(len(nums)):
            distinct[nums[end]] = distinct.get(nums[end],0) +1
            while len(distinct) >2:
                distinct[nums[start]] -=1
                if distinct[nums[start]] == 0:
                    del distinct[nums[start]]
                start+=1
            best = max(best,end-start +1)
        return best


        

