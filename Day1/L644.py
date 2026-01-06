# given an integer array nums and an integer k, find continuous subarrays whose length atleast k and that has maximum possible average value. return the maximum average value of the subarrays. here sliding window doesnot work as the size is not fixed..and in sliding window we only compare (from a specific point start to a specific).. but in this problem many start point .. ending to specific end point but ensuring the length > k:

"""
Docstring for L644

convert the problem does any subarray with length > k have avg mid. if yes then we should check for higher avg... coverting problem into summation and binary search. (monotonic)
"""
class solution:
    def findmaxAverage(self,nums,k):
        # 1<=k<=len(nums)
        # nums[i] --> +,-,0
        def canweget(mid,nums):
            current_sum = sum(nums[:k])-k*mid 
            if current_sum >= 0:
                return True
            prefix_sum = 0
            min_prefix_sum = 0
            for i in range(k,len(nums)):
                current_sum += nums[i]-mid
                prefix_sum += nums[i-k] -mid
                min_prefix_sum = min(min_prefix_sum,prefix_sum) # will be the start of that subarray.
                if current_sum >= min_prefix_sum: # will end of that subarray.
                    return True
            return False
        
        lo,hi = min(nums),max(nums)
        mid = (lo+hi)/2
        eps = 1e-5
        while hi-lo > eps:
            if canweget(mid):
                lo = mid
            else:
                hi = mid
        return lo



        




        