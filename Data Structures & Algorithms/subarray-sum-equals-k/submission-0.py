class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0:1}
        res = 0
        prefix_sum = 0
        for i in nums:
            prefix_sum+=i
            if prefix_sum-k in prefix_map:
                res+=prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum,0)+1
        return res
            
        