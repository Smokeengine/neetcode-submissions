class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l=0
        r=1
        k=1
        while r<=len(nums)-1:
            if nums[l]!=nums[r] and l<r:
                l+=1
                r+=1
                k+=1
                print(nums)
            else:
                nums.pop(r)
                print(k)
        return k
      