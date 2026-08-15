class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(cur,total,i):
            if total == target:
                res.append(cur[:])
                return 
            if total > target or i == len(candidates):
                return
            cur.append(cadidates[i])
            dfs(cur,total+candidates[i],i+1)
            
            cur.pop()
            while i < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(cur,total,i+1)
        dfs([],0,0)
        return res
