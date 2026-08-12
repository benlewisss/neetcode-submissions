class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for bracket in s:
            if len(stack) == 0:
                stack.append(bracket)
            elif (bracket == ")") & (stack[-1] == "("):
                stack.pop()
            elif (bracket == "}") & (stack[-1] == "{"):
                stack.pop()
            elif (bracket == "]") & (stack[-1] == "["):
                stack.pop()
            else:
                stack.append(bracket)
            
            print(stack)

        return len(stack) == 0