class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = len(word1), len(word2)
        res = []
        for k in range(max(i, j)):
            if k < i:
                res.append(word1[k])
            if k < j:
                res.append(word2[k])
        return ''.join(res)