class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxres,minres = 1,1
        for num in nums:
            tmp = maxres * num
            maxres = max(num,num*maxres,minres*num)
            minres = min(num,tmp,minres*num)
            res = max(res,maxres)
        return res
