# maximum consecutive 1's (can swap atmost k 0 to 1 )


class solution:
    def longestOnes(self,nums,k):
        n = len(nums)
        start = 0
        zeros = 0
        best = 0

        for end in range(n):
            if nums[end] == 0:
                zeros +=1
            while zeros > k:
                if nums[start]==0:
                    zeros -=1
                start +=1
            best = max(best,end-start+1)
        return best

                

                
            
        



