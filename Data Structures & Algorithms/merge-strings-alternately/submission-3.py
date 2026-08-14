class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = len(word1)
        j = len(word2)
        s = []
        for w in range(max(i,j)):
            if w < i:
                s.append(word1[w])
            if w < j:
                s.append(word2[w])
        return "".join(s)


        # while l < len(word1) and l < len(word2):
        #     s.append(word1[l])
        #     s.append(word2[l])
        #     l += 1
        # s.append(word1[l:])
        # s.append(word2[l:])
        # return "".join(s)