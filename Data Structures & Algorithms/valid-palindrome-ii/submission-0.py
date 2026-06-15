class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                # check by removing one char from first non matching char pair
                skip_left_char, skip_right_char = s[i+1:j+1], s[i:j]
                return (skip_left_char==skip_left_char[::-1] 
                or skip_right_char==skip_right_char[::-1])
            # update i or j values
            i, j = i+1, j-1
        return True
