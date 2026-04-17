class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums)<=1:
                return nums
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            left = mergeSort(left)
            right = mergeSort(right)
            return merge(left, right)

        def merge(left,right):
            i,j=0,0
            res=[]
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            while i < len(left):
                res.append(left[i])
                i+=1
            while j < len(right):
                res.append(right[j])
                j+=1
            return res
        return mergeSort(nums)


        