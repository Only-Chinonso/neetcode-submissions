class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = max(piles)
        while l <= r:
            hour = 0
            k = (r + l) // 2
            for p in piles:
                hour += math.ceil(p / k)
            if hour <= h:
                res = min(res,k)
                l = k + 1
            else:
                r = k - 1
        return res
        