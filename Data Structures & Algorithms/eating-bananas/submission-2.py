class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)  
        res = r

        while l <= r:
            mid = (l + r) // 2
            total = sum(math.ceil(p / mid) for p in piles)
            if total <= h:  
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res