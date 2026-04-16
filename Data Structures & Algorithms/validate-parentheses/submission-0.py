class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n %2 != 0 or not s:
            return False
        
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                if len(stack) == 0:
                    return False
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                else:
                    return False
        if len(stack) ==0 :
            return True
        else:
            return False


        