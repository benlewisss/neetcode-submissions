from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        permutation = [0] * 26
        window_size = len(s1)
        for char in s1:
            permutation[ord(char) - 97] += 1
        
        window = [0] * 26
        s2_size = len(s2)

        if s2_size < window_size:
            return False

        for i in range(window_size):
            window[ord(s2[i]) - 97] += 1

        for i in range(s2_size - window_size + 1):
            if (window == permutation):
                return True
            
            window[ord(s2[i]) - 97] -= 1
            window[ord(s2[min(s2_size-1,i+window_size)]) - 97] += 1
            
        return False
