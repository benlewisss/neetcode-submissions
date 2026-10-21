class Solution:
    # I believe this solution is working (just too slow), did in 25 minutes. Continuation in solution 2
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        # Termination conditions: In order to be able to make a square, the sum of the array has to be divisible by 4
        # Also, this is calculated so we know the required length of each side for termination condition inside backtrack

        matchsticks_sum = sum(matchsticks)
        is_divisible = (matchsticks_sum % 4 == 0)
        if not is_divisible:
            return False

        required_side_length = matchsticks_sum // 4

        # Keep track of which matchsticks have been used.
        # If, after having picked a matchstick, we cannot pick another 
        # that is <= required_side_length for a given side, then we can't make a square
        cache = dict()
        def backtracking(curr_side: int, num_sides: int, used: list):
            if num_sides == 4:
                return True
            
            if tuple(used) in cache:
                return cache[tuple(used)]

            possible = False
            for i in range(len(matchsticks)):
                if used[i]:
                    continue
                
                if curr_side + matchsticks[i] == required_side_length:
                    used[i] = True
                    possible = possible or backtracking(0, num_sides + 1, used)
                    used[i] = False

                elif curr_side + matchsticks[i] < required_side_length:
                    used[i] = True
                    possible = possible or backtracking(curr_side + matchsticks[i], num_sides, used)
                    used[i] = False

            cache[tuple(used)] = possible
            return possible
            
        return backtracking(0, 0, [False] * len(matchsticks))