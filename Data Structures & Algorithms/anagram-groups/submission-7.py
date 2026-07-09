from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = defaultdict(list)
        for st in strs:
            sign = "".join(sorted(st))
            new[sign].append(st)

        return list(new.values())
        