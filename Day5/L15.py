# 3 sum such that sum(triplets) ==0: no two index can be same.

class Solution:
    def threeSum(self,nums):
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(0,n-2):
            if i> 0 and nums[i] ==nums[i-1]:
                continue
            ele = nums[i]
            left= i+1
            right = n-1
            while left < right:
                total = ele + nums[left] + nums[right]
                if  total== 0:
                    ans.append([ele,nums[left],nums[right]])
                    left +=1
                    right-=1
                    while left < right and nums[left]==nums[left-1]:
                        left +=1
                    while left < right and nums[right] ==nums[right+1]:
                        right-=1
                elif total < 0:
                    left+=1
                else:
                    right-=1

        return ans
                
                    
# from collections import Counter
# with counter i am not able to remove the duplicates properly.
# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         n = len(nums)
#         if n < 3:
#             return []
        
#         ans = []
#         d = Counter(nums)
        
#         for i in range(n - 2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue  # skip duplicates
            
#             d[nums[i]] -= 1
            
#             for j in range(i + 1, n):
#                 if j > i + 1 and nums[j] == nums[j-1]:
#                     continue  # skip duplicates
                
#                 d[nums[j]] -= 1
#                 target = -(nums[i] + nums[j])
                
#                 if d.get(target, 0) > 0:
#                     ans.append([nums[i], nums[j], target])
                
#                 d[nums[j]] += 1  # restore for next j
#             d[nums[i]] +=1

            
#             # d[nums[i]] += 1  # restore for next i
        
#         return ans

