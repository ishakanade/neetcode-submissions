class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        s = ''
        for i in strs:
            s += str(len(i)) + delimiter + i
        return s


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] !='#':
                j += 1
            len_str = int(s[i:j])
            strs.append(s[j+1: j+1+len_str])
            i = j+1+len_str
        return strs
