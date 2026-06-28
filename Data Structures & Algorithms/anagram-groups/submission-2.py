class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= {}
        for word in strs:
            w="".join(sorted(word))
            if w in res.keys():
                res[w].append(word)
            else:
                res[w]=[]
                res[w].append(word)
        return list(res.values())
                