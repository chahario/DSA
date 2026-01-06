# subarrays with K different Integers. 
# given a array Nums and a int K , return the number of good subarrays ( k different integers exactly equal to k).
## Approach : atmost k distinct integers in a subarray.
## Exactly K distinct = atmost K distinct - atmost K-1 distinct
# because atmost k is easy to count in a sliding window.

class Solution:
    def subarrayswithkDistinct(nums,k):
        def atmost(nums,k): # atmost k 
            ans = 0
            start = 0
            d = {}
            distinct = 0
            for end,ch in enumerate(nums):
                if ch not in d or d[ch]==0:
                    distinct +=1
                d[ch] = d.get(ch,0) +1

                while distinct > k:
                    left = nums[start]
                    d[left] -=1
                    if d[left]==0:
                        distinct-=1
                    start+= 1
                ans += end-start+1 # all substring ending at end , and starting from i [start,end]

            return ans
        return atmost(nums,k) - atmost(nums,k-1)


                
                
nums = [1,2,1,2,3]
k = 2
# ans = 7
print(Solution.subarrayswithkDistinct(nums,k))


## approach 2
# 
            

