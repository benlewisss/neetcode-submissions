from collections import deque
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for token in tokens:
            if token == '+':
                first_val = stack.pop()
                second_val = stack.pop()
                val = first_val + second_val
                stack.append(val)
            elif token == '-':
                first_val = stack.pop()
                second_val = stack.pop()
                val = second_val - first_val
                stack.append(val)
            elif token == '*':
                first_val = stack.pop()
                second_val = stack.pop()
                val = first_val * second_val
                stack.append(val)
            elif token == '/':
                first_val = stack.pop()
                second_val = stack.pop()
                val = math.trunc(second_val / first_val)
                stack.append(val)
            else:
                stack.append(int(token))

            
            
        return stack.pop()
            
