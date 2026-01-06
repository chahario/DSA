# given 2 string s and t of length m and n , return the min window substring of s s.t. every char of t is in that substring: no such substring return "".

import math
class solution:
    def minWindow(self,s,t):
        
        def helper(sd,td):
            # whether d1 >= d2 ,
            for ch,cnt in td.items():
                if sd.get(ch,0) < cnt:
                    return False
            return True 
        start = 0
        best = 10**6    
        td = {}
        sd = {}
        ans= ""
        for i in range(len(t)):
            td[t[i]] = td.get(t[i],0) +1
        for end in range(len(s)):
            if s[end] in td:
                sd[s[end]] = sd.get(s[end],0) +1
            while helper(sd,td):
                window_len = end-start +1
                if window_len < best:
                    best = window_len
                    ans = s[start:end+1]

                if s[start] in td:
                    sd[s[start]] -=1
                start+=1
        return ans

            
        




        
