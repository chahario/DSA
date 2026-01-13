# subarray product < k
# find the max 
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k<=1:
            return 0
        ans = 0
        product =1
        start = 0
        for end in range(n):
            product = product * nums[end]
            while product>=k: # start< end and product >=k
                product = product/nums[start]
                start+=1
            if product < k:
                ans +=(end-start +1)
        return ans
            
            
"""start < end is not a safety check

It breaks the sliding-window invariant

Correctness comes from restoring validity, not from index conditions"""