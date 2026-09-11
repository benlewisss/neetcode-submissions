from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window_size = len(s1)
        window = Counter(s1)

        target_size = len(s2)

        if target_size < window_size:
            return False

        for i in range(target_size - window_size + 1):
            if Counter(s2[i:i+window_size]) == window:
                return True
        
        return False
