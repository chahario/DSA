# two sum
class solution:
    def twosum(nums, k):
        d = {}
        for idx,x in enumerate(nums):
            if x not in d:
                d[x] = [idx]
            else:
                d[x].append(idx)
        nums.sort()
        l,r = 0 , len(nums)-1
        while l<r:
            if nums[l] + nums[r] == k:
                if nums[l] == nums[r]:
                    return d[nums[l]][:2]
                return [d[nums[l][0]],d[nums[r][0]]]
            elif nums[l] + nums[r] > k:
                r-=1
            else:
                l+=1
        return -1
## approach 2

class solution2:
    def twosum(nums,k):
        d = {}
        for idx,x in enumerate(nums):
            if k - x in d:
                return [d[k - x], idx]
            d[x] = idx
        return -1