# maximum number of vowels in a substring of given length k
class solution:
    def maxVowels(self, s, k):
        # 1 <= k <= s.length
        start = end = 0
        count = 0
        d = {'a':1,'e':1,'i':1,'o':1,'u':1}
        while end - start < k :
            if s[end] in d:
                count+=1
            end+=1
        max_count = count # any k th window can have the max vowels so need to take the max of it.
        while end < len(s):
            if s[end] in d:
                count+=1
        
            if s[start] in d:
                count -=1
            start+=1
            end +=1
            max_count = max(max_count,count)
            if max_count == k:
                return k 
        return max_count
            


# solution 2

class Solution2:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        k = min(k, n)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = count
        if max_count == k:
            return k

        for i in range(k, n):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            if count > max_count:
                max_count = count
                if max_count == k:
                    return k

        return max_count


