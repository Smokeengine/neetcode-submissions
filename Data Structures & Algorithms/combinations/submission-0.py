class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(n):
            arr.append(i+1)
        res = []
        def helper(i, cur):
            if len(cur) == k:
                res.append(list(cur))
                return
            if i >= n :
                return
            
            cur.append(arr[i])
            helper(i+1, cur)

            cur.pop()
            helper(i+1, cur)
        helper(0, [])
        return res
            


        