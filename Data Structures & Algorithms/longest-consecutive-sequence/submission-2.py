class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        length = 0
        for i in nums_set:
            if i-1 not in nums_set:
                cur_num = i
                cur_len = 1
                while (cur_num+1) in nums_set:
                    cur_num+=1
                    cur_len+=1
                length = max(length,cur_len)
        return length
        