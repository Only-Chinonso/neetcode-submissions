class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        maxn = 0
        for r in range(k,len(nums)):
            for num in nums[l:r]:
                maxn = max(maxn,num)
            res.append(maxn)
            maxn = 0
            l += 1
        return res
