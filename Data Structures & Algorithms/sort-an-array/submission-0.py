class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>= nums[j]:
                    temp =nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        return nums

        