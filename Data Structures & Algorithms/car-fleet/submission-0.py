class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p , s in zip(position, speed)]
        stack = []
        print(sorted(pairs)[::-1])
        for p, s in sorted(pairs)[::-1] :
            
            time = (target - p) / s
            stack.append(time)
            print(stack[-1])
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()
        return len(stack)
        