"""
Docstring for Day2.L03

longest substring without repeating characters
"""
# variable silding window length .. start pointer moves based on the condition and any steps.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        start = 0
        best = 0
        for end, ch in enumerate(s):
            if ch in last and last[ch] >= start:
                start = last[ch] +1

            last[ch] = end

            best = max(best, end-start +1)
        return best



    