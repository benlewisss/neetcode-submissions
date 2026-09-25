class Solution:
    # 40 mins to reach naive backtrack solution myself (+ got a hint for a stupid little bug forgetting to .pop() after second backtrack option (2 digit add) step.)

    # 60 minutes to finalise whole thing - got a couple hints to fix bugs because I'm tired, but the meat of it was me.
    def numDecodings(self, s: str) -> int:
        cache = collections.defaultdict()
        def backtrack(digit_pointer):
            if digit_pointer >= len(s):
                return 1

            if s[digit_pointer] == '0':
                return 0

            if digit_pointer not in cache:
                num_ways = 0
                if int(s[digit_pointer : digit_pointer + 1]) <= 26:
                    num_ways += backtrack(digit_pointer + 1)
        
                if digit_pointer + 1 < len(s):
                    if int(s[digit_pointer : digit_pointer + 2]) <= 26:
                        num_ways += backtrack(digit_pointer + 2)

                cache[digit_pointer] = num_ways

            return cache[digit_pointer]

        return backtrack(0)





