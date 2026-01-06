# group anagrams from a list of strings
from collections import defaultdict
from typing import List
class solution: 
    def groupAnagrams(strs):
        anagramas = defaultdict(list)
        for ch in strs:
            key = ''.join(sorted(ch))
            anagramas[key].append(ch)
        return list(anagramas.values())

        
            
