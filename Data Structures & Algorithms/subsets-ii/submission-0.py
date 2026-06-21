class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def helper(i, cur):
            if i>= len(nums):
                res.add(tuple(cur))
                return
            # picking the element
            cur.append(nums[i])
            helper(i+1, cur)

            #not-pick the element
            cur.pop()
            helper(i+1, cur)
        nums.sort()
        helper(0, [])
        return [list(s) for s in res]
        