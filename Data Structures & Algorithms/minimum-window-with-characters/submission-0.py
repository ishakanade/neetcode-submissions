class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == '':
            return ""

        left = 0
        matches = 0
        count = defaultdict(int)
        window = defaultdict(int)

        for ch in t:
            count[ch] += 1

        result = ""         # stores the minimum window
        min_len = float("inf")  # tracks length of the minimum window

        for right in range(len(s)):
            # if s[right] in count:
            window[s[right]] += 1
            if s[right] in count and window[s[right]] == count[s[right]]:
                matches += 1

            # Shrink window while valid
            while matches == len(count):
                # Update result if current window is smaller
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]

                # Shrink from left
                window[s[left]] -= 1
                if s[left] in count and window[s[left]] < count[s[left]]:
                    matches -= 1
                left += 1

        return result