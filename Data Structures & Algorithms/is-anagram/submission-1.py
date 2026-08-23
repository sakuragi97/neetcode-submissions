class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for s_char, t_char in zip(s, t):
            count[s_char] = count.get(s_char, 0) + 1
            count[t_char] = count.get(t_char, 0) - 1
        return all(v == 0 for v in count.values())
