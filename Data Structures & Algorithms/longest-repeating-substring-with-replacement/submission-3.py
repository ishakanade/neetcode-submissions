class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        result = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            curr_str = r - l + 1
            while(curr_str - maxf > k):
                count[s[l]] -=1
                l+=1
                curr_str = r - l + 1
            result = max(result, curr_str)
        
        return result
