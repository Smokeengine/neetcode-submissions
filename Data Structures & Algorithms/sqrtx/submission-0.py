class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0 , x
        while low <= high:
            mid = (low + high) // 2
            res = mid ** 2
            if res == x:
                return mid
            elif x < res:
                high = mid - 1
            else:
                low = mid + 1
        return high
        