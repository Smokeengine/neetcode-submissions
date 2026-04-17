class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}  # stores {value: index}
    
        for i, num in enumerate(numbers):
            diff = target - num
            
            if diff in seen:  # check if complement exists
                return [seen[diff] + 1, i + 1]  # +1 for 1-indexed
            
            seen[num] = i  # store value as key, index as value
        
        return []
        