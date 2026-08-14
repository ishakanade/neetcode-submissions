class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)==0:
            return []
        i = 0
        j = len(s) - 1
        # for schar in range(len(s)//2):
        #     s[i], s[j] = s[j], s[i]
        #     i +=1
        #     j -=1
        while j > i:
            s[i], s[j] = s[j], s[i]
            i +=1
            j -= 1
        return s
        