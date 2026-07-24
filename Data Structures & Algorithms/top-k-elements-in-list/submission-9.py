class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        fre = 0
        number = 0
        for _ in range(k):
            for n in nums :
                if nums.count(n) > fre :
                    fre = nums.count(n)
                    number = n
            res.append(number)
            nums.remove(number)
            fre = 0
            number = 0
        return res
                