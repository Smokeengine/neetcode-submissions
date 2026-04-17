class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        nums_set = set(nums)
        c=1

        while c in nums_set:
            c+=1

        return c
        



        