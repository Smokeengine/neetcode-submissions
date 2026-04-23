class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        maxl = float('inf')
        count = 0
        
        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                maxl = min(maxl, r-l+1)
                count -= nums[l]
                l+=1
            r+=1
        return maxl if maxl!= float('inf') else 0
            
        