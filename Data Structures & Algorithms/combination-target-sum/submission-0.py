class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        summ = i = 0
        n = len(nums)
        ds = []
        self.helper(i, n, summ, target, nums, res, ds)
        return ds

    def helper(self, i, n, summ, target, nums, res, ds):
        if (i>=n) or summ > target:
            return
        if summ == target:
            ds.append(res[:])
            return
        
        res.append(nums[i])
        summ += nums[i]
        self.helper(i, n, summ, target, nums, res, ds)

        res.pop()
        summ -= nums[i]
        self.helper(i+1, n, summ, target, nums, res, ds)



        