# longest substring with atmost two distinct characters. 
# varying sliding window problem 

class solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count = 0
        d ={}
        start = end =0 # here int is immutable but for mutable this is wrong (like list).. both point to the same reference. 
        while end < len(s):
            d[s[end]] = d.get(s[end],0)+1
            while len(d) > 2: # here while works as i need to remove all the characters until the condition is satisfied.
                d[s[start]] -=1
                if d[s[start]] == 0:
                    del d[s[start]]
                start +=1
            count = max(count, end-start +1)
            end+=1
        return count
    


            




