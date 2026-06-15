class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        left = 0
        max_freq = 0
        longest = 0
        # BBAAABAA
        for i in range(len(s)):
            window[s[i]] = 1+ window.get(s[i],0)
            max_freq = max(window.values())
            while ((i - left + 1) - max_freq > k):
                window[s[left]] -= 1
                left +=1
            longest = max(longest, i - left + 1) 

        return longest
            



            
