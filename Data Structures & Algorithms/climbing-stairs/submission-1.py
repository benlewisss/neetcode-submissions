from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:

        def memoization(num_steps: int, cache = defaultdict()) -> int:
            if num_steps <= 2:
                return num_steps
            
            if num_steps in cache:
                return cache[num_steps]

            cache[num_steps] = memoization(num_steps - 1, cache) + memoization(num_steps - 2, cache)
            return cache[num_steps]

                
        return memoization(n)
            

