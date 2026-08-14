class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return (skipL == skipL[::-1]) or (skipR == skipR[::-1])
            l += 1
            r -= 1
        return True
        '''
        def palindromehelper(hi, lo):
            while hi<lo:
                if s[hi] != s[lo]:
                    return False
                hi += 1
                lo -= 1
            return True

        l, r = 0 , len(s)-1
        while l < r:
            if s[l] != s[r]:
                return (palindromehelper(l+1, r) or palindromehelper(l, r-1))
            l += 1
            r -= 1
        return True
        '''