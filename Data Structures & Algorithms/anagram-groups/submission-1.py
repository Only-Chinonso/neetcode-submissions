class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}#{word.sort():word}
        res = []
        for word in strs :
            if word in ana :
                ana[sorted(word)].append(word)
            else :
                ana[sorted(word)] = word
        for value in ana.value():
            res.append(list(value))
        return res
        