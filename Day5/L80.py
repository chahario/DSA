# remove duplicates from an sorted array

"""
Docstring for Day5.L80

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
# the left pointer should keep upto duplicates:
class Solution:
    def removeDuplicates(self,nums):
        n = len(nums)
        if n <=2:
            return n
        j =2
        for i in range(2,n):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j +=1
        return j
class Solution2:
    def removeDuplicates(self,nums):
        n = len(nums)
        if n <=2:
            return n
        l,r =0,0
        while r <n:
            count =1
            while r+1 < n and nums[r] ==nums[r+1]:
                count+=1
                r+=1
            for i in range(min(2,count)):
                nums[l] = nums[r]
                l+=1
            r+=1
        return l
