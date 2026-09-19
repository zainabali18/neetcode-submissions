from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = tuple(sorted(Counter(s).items()))
            anagrams[count].append(s)
        return list(anagrams.values())