class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for num in numbers:
            diff = target - num
            if diff in numbers:
                res.append(diff)
                res.append(num)
                res = set(res)
                res = list(res)
                return res