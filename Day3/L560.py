# number of subarrays sum equal to K

class solution:
    def subarraySum(nums,k):
        if len(nums)==1:
            if nums[0]==k:
                return 1
            return 0
        l = [0]*(len(nums)+1)
        for i in range(len(nums)):
            l[i+1] = l[i]+ nums[i]
        ans = 0
        start = 0
        d = {}
        for end in range(len(l)):
            d[l[end]] = d.get(l[end],0)+1
            if k!=0:
                if l[end] - k in d:
                    ans += d[l[end]-k]
            else:
                ans += d[l[end]]-1
        return ans


            
            
