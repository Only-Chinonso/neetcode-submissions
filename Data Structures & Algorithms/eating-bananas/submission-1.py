class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        hour = 0
        res = max(piles)
        while l <= r:
            k = (r + l) // 2
            for p in piles:
                hour += math.ceil(p / k)
            if hour <= h:
                res = min(res,hour)
                l = k + 1
            else:
                r = k - 1
        return res
        