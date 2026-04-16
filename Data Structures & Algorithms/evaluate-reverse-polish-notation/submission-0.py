class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                t1 = stack.pop(-1)
                t2 = stack.pop(-1)
                stack.append(int(t1 + t2))
            elif i == '-':
                t1 = stack.pop(-1)
                t2 = stack.pop(-1)
                stack.append(int( t2 - t1))
            elif i == "*":
                t1 = stack.pop(-1)
                t2 = stack.pop(-1)
                stack.append(int(t1 * t2))
            elif i == "/":
                t1 = stack.pop(-1)
                t2 = stack.pop(-1)
                stack.append(int( t2 / t1))
            else:
                stack.append(int(i))
        return stack[-1]
        