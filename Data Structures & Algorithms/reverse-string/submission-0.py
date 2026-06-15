class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)==0:
            return []
        i = 0
        j = len(s)-1
        while j > i:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j -= 1
            i += 1
        print("final", s)
        return s
        