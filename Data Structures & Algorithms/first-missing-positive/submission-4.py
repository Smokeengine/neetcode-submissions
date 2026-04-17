class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        res = {}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        res = sorted(res)
        c=1
        for i in res:
            if i==0:continue
            elif i == c:
                c+=1
            else:
                break
        return c

         



        