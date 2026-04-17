class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
    
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            
            if curr_sum == target:
                return [l + 1, r + 1]  # 1-indexed
            elif curr_sum < target:
                l += 1  # need bigger sum, move left pointer right
            else:
                r -= 1  # need smaller sum, move right pointer left
        
        return []
            
        