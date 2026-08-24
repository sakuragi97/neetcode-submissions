class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for item in strs:
            key = tuple(sorted(item))
            anagrams[key].append(item)
        return list(anagrams.values())
        