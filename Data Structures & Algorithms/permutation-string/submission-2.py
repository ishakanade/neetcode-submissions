class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        window = {}
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        l = 0
        for r in range(len(s2)):
            if s2[r] not in count:
                window.clear()
                l = r + 1
            else:
                window[s2[r]] = window.get(s2[r], 0) + 1
                while window.get(s2[r], 0) > count.get(s2[r], 0):
                    window[s2[l]] -= 1
                    l += 1
                if r - l + 1 == len(s1):
                    return True
        return False

        # count = {}
        # window = {}

        # for i in range(len(s1)):
        #     count[s1[i]] = 1 + count.get(s1[i], 0)

        # l = 0

        # for r in range(len(s2)):
        #     if s2[r] not in count:
        #         window.clear()
        #         l = r + 1
        #     else:
        #         window[s2[r]] = window.get(s2[r], 0) + 1

        #         while window.get(s2[r], 0) > count.get(s2[r], 0):
        #             window[s2[l]] -= 1
        #             l += 1

        #         if r - l + 1 == len(s1):
        #             return True

        # return False