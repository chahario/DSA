# given an unsorted array find the length of longest consecutive elements sequence.

class solution:
    def longestConsecutive(self,nums):
        numset = set(nums)
        max_count = 0
        for ele in numset:
            if ele-1 not in numset: # iterate over the unique elements not on the array . it starting from the each sequence (smallest first)
                length = 0
                while ele + length in numset:
                    length +=1
                max_count = max(max_count,length)
        return max_count





        


        

        
        