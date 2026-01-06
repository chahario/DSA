# Subarray of size k with the avgerage >= threshold


class Solution :
    def numberofSubarrays(self,arr,k ,threshold):
        # k>=1 and threshold>=0 and length >=1


        """
        first check for the first k elements (if k > n return 0 , else check if the first set of k elements statisfy the condition if yes increase the count else move to the next elements ( note : after first element loops end will at k so total element will be (k+1)))
        """
        count = 0
        start = 0
        end = 0
        summation = 0
        length = len(arr)
        while (end-start < k) and (end < length):
            summation += arr[end]
            end +=1
        if end - start !=k:
            return 0
        if summation /k >= threshold:
            count+=1
        while end < length:
            summation += arr[end] -arr[start]
            end+=1
            start+=1
            if summation /k >= threshold:
                count+=1
        return count
    

# solution 2
# here the length of sliding window is same ==k:
class solution2:
    def numberofsubarrays(self, arr, k , threshold):
        summation = sum(arr[:k])
        count =0 
        n = len(arr)
        if summation / k >= threshold:
            count +=1
        for end in range(k,n):
            summation += arr[end] - arr[end-k]
            if summation/k >= threshold:
                count+=1
        return count
