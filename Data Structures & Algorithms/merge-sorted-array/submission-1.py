class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m ==0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
        for i in range(n):
            nums1[m] = nums2[i]
            m+=1
        nums1 = self.heapSort(nums1)
    def heapSort(self,nums):
        n = len(nums)
        for i in range((n//2)-1,-1,-1):
            self.heapify(nums,n,i)
        for i in range(n-1,0,-1):
            nums[0],nums[i]= nums[i],nums[0]
            self.heapify(nums,i,0)
        return nums
    def heapify(self,nums,n,i):
        lar = i
        l=2*i+1
        r=2*i+2
        if l<n and nums[l]>nums[lar]:
            lar=l
        if r<n and nums[r]>nums[lar]:
            lar=r
        if lar!=i:
            nums[i],nums[lar] = nums[lar],nums[i]
            self.heapify(nums,n,lar)





        