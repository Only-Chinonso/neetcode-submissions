class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        dp = set()
        dp.add(0)
        for num in nums:
            tmp = set()
            for a in dp:
                if a == target:
                    return True
                tmp.add(a)
                tmp.add(a + num)
            dp = tmp
        if target in dp:
            return True
        return False

