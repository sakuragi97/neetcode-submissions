class Solution:

    def encode(self, strs: List[str]) -> str:
        join_str=""
        for word in strs:
            word_len = len(word)
            join_str += str(word_len)+"#" + word
        return join_str

    def decode(self, s: str) -> List[str]:
        list_str = []
        left=0
        left = 0
        while left < len(s):
            right=left
            while s[right] != '#':
                right+=1
            word_len = int(s[left:right])
            word = s[right+1:right+word_len+1]
            list_str.append(word)
            left = right + word_len + 1
        return list_str