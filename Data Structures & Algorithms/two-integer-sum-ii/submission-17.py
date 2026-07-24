class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for num in numbers:
            diff = target - num
            if diff in numbers:
                lst = numbers.index(diff) + 1, numbers.index(num) + 1
                res.append(lst)
                res = set(res)
                res = list(res)
                return sorted(res)