class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        fre = 0
        for _ in range(k):
            for n in nums :
                if nums.count(n) > fre :
                    fre = n
            res.append(fre)
            nums.remove(fre)
            fre = 0
        return res
                