class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        window = {}
        for i in t:
            count[i] = 1 + count.get(i, 0)
        l = 0
        matches = 0
        result=""
        min_len = float('inf')
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in count and count[s[r]] == window[s[r]]:
                matches+=1
            while matches == len(count):
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    result = s[l:r+1]
                window[s[l]]-=1
                if s[l] in count and count[s[l]] > window[s[l]]:
                    matches-=1
                l+=1
        return result