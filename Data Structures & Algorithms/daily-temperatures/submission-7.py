class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l ,r= 0,0
        cnt = 0
        res = []
        while l < len(temperatures):
            while temperatures[r] < temperatures[l] and l < len(temperatures):
                cnt += 1
                r += 1
            res.append(cnt)
            r = l + 1
            cnt = 0
            l += 1
        return res