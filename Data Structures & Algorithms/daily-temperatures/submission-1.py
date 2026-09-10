# Watched solution explanation, just programmed mysself
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((temp, idx))
                continue

            while stack and temp > stack[-1][0]:
                res[stack[-1][1]] = idx - stack[-1][1]
                stack.pop()
            
            stack.append((temp, idx))

        return res
