class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, res):
            if i >= len(nums):
                res.append(list(nums))
                return
            
            for j in range(i,len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1, res)
                nums[i], nums[j] = nums[j], nums[i]

        helper(0, res)
        return res
