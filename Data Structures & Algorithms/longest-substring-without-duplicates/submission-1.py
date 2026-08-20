class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_substr = 0
        l = 0
        for i in range(len(s)):
            if s[i] in window:
                # need to remove from window until the curr char is not removed from the set
                while s[i] in window:
                    window.remove(s[l])
                    l += 1
            window.add(s[i])
            max_substr = max(max_substr, len(window))
        return max_substr