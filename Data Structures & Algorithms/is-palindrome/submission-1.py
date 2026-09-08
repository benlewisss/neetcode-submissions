class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1

        while (left_ptr < right_ptr):
            if not s[left_ptr].isalnum():
                left_ptr += 1
                continue
            if not s[right_ptr].isalnum():
                right_ptr -= 1
                continue
            
            if (s[left_ptr].lower() != s[right_ptr].lower()):
                return False
            
            left_ptr += 1
            right_ptr -= 1
            
        return True

            
            