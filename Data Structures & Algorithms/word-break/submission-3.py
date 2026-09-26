class Solution:
    # Solved ON MY OWN COMPLETELY in 10 MINUTES!!!!!!!!!!!!!!!!!! YES
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def backtrack(pointer):
            if pointer >= len(s):
                return True

            if (pointer not in memo):
                res = False

                for word in wordDict:
                    if s[pointer:pointer+len(word)] == word:
                        res = res or backtrack(pointer+len(word))

                memo[pointer] = res

            return memo[pointer]

        return backtrack(0)