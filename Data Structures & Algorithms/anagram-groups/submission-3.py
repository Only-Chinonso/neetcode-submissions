class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}#{word.sort():word}
        res = []
        for word in strs :
            key = "".join(sorted(word))
            if key in ana :
                ana[key].append(word)
            else :
                ana[key] = word
        for value in ana.values():
            res.append(value)
        return res
        