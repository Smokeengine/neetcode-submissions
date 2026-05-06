class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for num in nums:
        #     if(num in seen):
        #         return True
        #     seen.add(num)
        # return False
        seen = set(nums)
        if len(nums) == len(seen):
            return False
        return True