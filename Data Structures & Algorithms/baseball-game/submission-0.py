class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for i, n in enumerate(operations):
            if n == "+" :
                stack.append(int(stack[-1])+int(stack[-2]))
            elif n == "C":
                stack.pop()
            elif n == "D" :
                stack.append(int(stack[-1])*2)
            else:
                stack.append(int(n))
                print(n)
        for i in stack:
            total += i
        return total



        