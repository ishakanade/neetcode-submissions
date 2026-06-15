class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        left = 0
        max_freq = 0
        longest = 0
        for i in range(len(s)):
            window[s[i]] = 1+ window.get(s[i],0)
            max_freq = max(max_freq, window[s[i]])
            window_len = i - left + 1
            # longest = max(longest, window_len)
            while (window_len - max_freq > k):
                window[s[left]] = window.get(s[left], 0) - 1
                left +=1
                window_len -=1 
            longest = max(longest, window_len) 

        return max(longest, window_len)
            



            
