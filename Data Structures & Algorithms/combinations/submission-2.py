class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(i, cur):
            if len(cur) == k:
                res.append(list(cur))
                return
            if n-i < k - len(cur): #n-i is the remaining ele and k - len(cur) is needed
                return              #if remaining is less than needed no need to dig down
            cur.append(i+1)
            helper(i+1, cur)

            cur.pop()
            helper(i+1, cur)
        helper(0, [])
        return res
            


        