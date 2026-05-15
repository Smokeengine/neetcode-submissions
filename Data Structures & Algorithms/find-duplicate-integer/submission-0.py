class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = defaultdict(int)
        ans = 0
        for i in nums:
            res[i] += 1
        for i in res:
            if res[i] > 1:
                ans = i
        return ans
        
            
        