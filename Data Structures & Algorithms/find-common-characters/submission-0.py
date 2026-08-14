class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = counter(words[0])
        for w in words:
            cur_cnt = counter(w)
            for c in cur_cnt:
                if c in cnt:
                    cnt[c] = min(cur_cnt[c],cnt[c])
        
        res = []
        for c in cnt:
            for _ in range(cnt[c]):
                res.append(c)
        return res