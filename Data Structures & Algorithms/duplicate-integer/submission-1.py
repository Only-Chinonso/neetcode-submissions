class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasmap = set()
        for num in nums :
            if num in hasmap :
                return True
            hasmap.add(num)
        return False