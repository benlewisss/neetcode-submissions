class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        def backtracking(i, curr_combination, need_close: int):
            if i >= n * 2:
                if need_close == 0:
                    output.append(''.join(curr_combination))
                return

            curr_combination.append('(')
            backtracking(i + 1, curr_combination, need_close + 1)
            curr_combination.pop()

            if need_close:
                curr_combination.append(')')
                backtracking(i + 1, curr_combination, need_close - 1)
                curr_combination.pop()

        backtracking(0, [], 0)
        return output