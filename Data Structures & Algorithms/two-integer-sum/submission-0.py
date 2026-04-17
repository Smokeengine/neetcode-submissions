class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                if (nums[j] == target - temp):
                    return [nums.index(temp), j]
            temp = nums[i]
        return []
            
        