class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l ,r= 0,0
        cnt = 0
        res = []
        while l < len(temperature):
            while temperature[r] < temperature[l] and r < len(temperature):
                cnt += 1
                r += 1
            res.append(cnt)
            r = 0
            cnt = 0
            l += 1
        return res