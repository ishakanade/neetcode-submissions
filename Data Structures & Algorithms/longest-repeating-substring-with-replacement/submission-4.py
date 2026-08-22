class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        result = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            curr_len = r-l+1
            maxf = max(maxf, count[s[r]])
            while (curr_len-maxf > k):
                count[s[l]] -= 1
                l+=1
                curr_len = r-l+1
            result = max(result, curr_len)
        return result