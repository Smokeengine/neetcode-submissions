class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        low, high = 0 , len(nums)-1
        while low <= high:
            if nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid + 1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
                break
        return -1

        