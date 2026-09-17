class Solution:
    # Completed on my own in 20 minutes - however, I actually did in 15 but my output was char arrays not strings, which I didn't realise so I had to figure out how to convert / avoid char arrays.
    def letterCombinations(self, digits: str) -> List[str]:
        dialpad = {'2': {'a','b','c'}, '3': {'d','e','f'}, '4': {'g','h','i'}, '5': {'j','k','l'}, '6': {'m','n','o'}, '7': {'p','q','r','s'}, '8': {'t','u','v'}, '9': {'w','x','y','z'}}
        all_combinations = []

        def backtrack(index, curr_string):
            if len(curr_string) == len(digits):
                all_combinations.append(curr_string)
                return

            if index >= len(digits):
                return

            for char in dialpad[digits[index]]:
                backtrack(index + 1, curr_string + char)

        backtrack(0, "")
        if len(all_combinations) == 1 and all_combinations[0] == "":
            all_combinations = []
        return all_combinations

            