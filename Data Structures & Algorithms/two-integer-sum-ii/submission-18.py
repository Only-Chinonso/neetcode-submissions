class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for num in numbers:
            diff = target - num
            if diff in numbers:
                lst2 = numbers.index(diff) + 1
                lst1 = numbers.index(num) + 1
                res.append(lst2)
                res.append(lst1)
                res = set(res)
                res = list(res)
                return sorted(res)