class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp = {}
        res = []
        for i in nums:
            if i in temp:
                temp[i]+=1
            else:
                temp[i]=1
        for num, freq in temp.items():
            if freq > len(nums)//3:
                res.append(num)
        return res
    
        