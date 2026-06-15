class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subarray = set()
        left_pointer = 0
        maxlen = 0
        for i in range(len(s)):
            while s[i] in subarray:
                subarray.remove(s[left_pointer])
                left_pointer +=1
            subarray.add(s[i])
            maxlen = max(maxlen, i-left_pointer+1)
        return maxlen