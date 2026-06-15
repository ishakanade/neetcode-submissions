class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        left = 0
        matches = 0
        count = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(s1)):
            count[s1[i]] +=1
        
        for right in range(len(s2)):
            if s2[right] in count:
                window[s2[right]] +=1
                if window[s2[right]] == count[s2[right]]:
                    matches +=1
    
            if right - left + 1 > len(s1):
                if s2[left] in count:
                    if window[s2[left]] == count[s2[left]]:
                        matches -=1
                    window[s2[left]] -=1
                left += 1

            if matches == len(count):
                return True
        
        return False