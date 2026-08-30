class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        max_length = 0

        R = 0
        L = 0

        while R < len(s):
            if s[R] in seen:
                seen.remove(s[L])
                L += 1
                continue

            max_length = max(max_length, (R - L) + 1)
            seen.add(s[R])
            R += 1

        return max_length