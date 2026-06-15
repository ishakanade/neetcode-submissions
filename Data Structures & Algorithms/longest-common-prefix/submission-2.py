class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs)==1):
            return strs[0]
        else:
            sortedstr = sorted(strs)
            first_word = sortedstr[0]
            last_word = sortedstr[-1]
            for i in range(min(len(first_word), len(last_word))):
                if first_word[i] != last_word[i]:
                    return first_word[:i]
        return first_word

        