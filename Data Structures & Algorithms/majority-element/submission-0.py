class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in nums:
            count[i]+=1
        for num, freq in count.items():
            if freq > len(nums) / 2:
                return num