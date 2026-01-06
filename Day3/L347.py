class solution:
    def topKFrequent(nums,k):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0) +1
        
        ans = sorted(d,key = d.get,reverse=True)[:k]
        return ans