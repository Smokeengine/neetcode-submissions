class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, cur):
            if i>= len(nums):
                res.append(list(cur))
                return
            # picking the element
            cur.append(nums[i])
            helper(i+1, cur)

            #not-pick the element
            cur.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, cur)
        nums.sort()
        helper(0, [])
        return res
        