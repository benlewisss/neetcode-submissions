class Solution:
    # Solved on my own in 20 minutes.
    def longestPalindrome(self, s: str) -> str:
        
        def get_longest_palindrome(i):
            L = R = i
            min_L, max_R = L, R

            # Odd length palindrome
            while L >= 0 and R < len(s) and s[L] == s[R]:
                min_L, max_R = min(min_L, L), max(max_R, R)
                L -= 1
                R += 1

            # Even length palindrome (from left middle)
            L = i
            R = i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                min_L, max_R = min(min_L, L), max(max_R, R)
                L -= 1
                R += 1

            # Even length palindrome (from right middle)
            L = i - 1
            R = i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                min_L, max_R = min(min_L, L), max(max_R, R)
                L -= 1
                R += 1

            return (min_L, max_R)

        longest_palindrome = 0
        longest_palindrome_L = longest_palindrome_R = 0

        for i in range(len(s)):
            L, R = get_longest_palindrome(i)
            if R - L + 1 > longest_palindrome:
                longest_palindrome = R - L + 1
                longest_palindrome_L = L
                longest_palindrome_R = R

        return s[longest_palindrome_L:longest_palindrome_R+1]

        