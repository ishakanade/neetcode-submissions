class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        s = []
        while l < len(word1) and l < len(word2):
            s.append(word1[l])
            s.append(word2[l])
            l += 1
        s.append(word1[l:])
        s.append(word2[l:])
        return "".join(s)