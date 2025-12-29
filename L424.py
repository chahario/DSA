# given s and k , change any letter to any other uppercase letter at most k times to get the longest possible substring of the same letter
# here the length can vary (sliding window) based on the cases.
class solution:
    def characterReplacement(self, s, k):
        start,end = 0,0
        count = 0
        d = {}
        while end < len(s):
            d[s[end]] = d.get(s[end],0)+1
            maxf = max(d.values())
            if (end-start+1) - maxf > k: # here if works
                d[s[start]] -=1
                start+=1
            count = max(count,end-start +1)
            end +=1
        return count
    
