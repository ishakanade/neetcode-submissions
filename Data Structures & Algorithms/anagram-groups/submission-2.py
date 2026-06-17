class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ord('a') = 97
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
            res[tuple(count)].append(s)
        return(list(res.values()))

        # res = defaultdict(list)
        # sorted_strs = sorted(strs)
        # for s in strs:
        #     sorted_str = ''.join(sorted(s))
        #     res[sorted_str].append(s)
        # return list(res.values())
