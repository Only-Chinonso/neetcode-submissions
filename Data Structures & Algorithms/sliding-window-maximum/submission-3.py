class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        maxn = -999999999
        for r in range(k,len(nums)+ 1):
            for num in nums[l:r]:
                maxn = max(maxn,num)
            res.append(maxn)
            maxn = 0
            l += 1
        return res
