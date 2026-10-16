class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(L: int, R: int, can_skip: bool = False):
            
            while L < R:
                if s[L] != s[R]:
                    if can_skip:
                        return (isPalindrome(L + 1, R, False) or isPalindrome(L, R - 1, False))
                    return False
                L += 1
                R -= 1
            return True


        return isPalindrome(0, len(s) - 1, True)