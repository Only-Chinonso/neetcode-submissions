class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}#{word.sort():word}
        res = []
        for word in strs :
            ana[sorted(word)].append(word)
        for value in ana.value():
            res.append(list(value))
        return res
        