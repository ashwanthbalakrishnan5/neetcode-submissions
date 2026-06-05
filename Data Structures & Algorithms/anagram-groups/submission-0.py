from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for i in range(len(strs)):
            counter = tuple(sorted(Counter(strs[i])))
            if counter in d:
                d[counter].append(strs[i])
                continue
            d[counter] = [strs[i]]
        return list(d.values())