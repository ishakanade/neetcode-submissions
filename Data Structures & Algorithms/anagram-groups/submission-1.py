class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = sorted(strs)
        # print(strs_sorted)
        strs_keys = defaultdict(list)
        for i in strs:
            sorted_str = ''.join(sorted(i))
            strs_keys[sorted_str].append(i)
        return list(strs_keys.values())
        # main_lst = []
        # i = 0
        # while i < (len(strs_sorted)):
        #     temp_lst = []
        #     temp_lst.append(strs_sorted[i])
        #     j = i+1
        #     while j < len(strs_sorted) and (strs_keys[i] == strs_keys[j]):
        #         temp_lst.append(strs_sorted[j])
        #         j += 1
        #     main_lst.append(temp_lst)
        #     i = j
        # # print(main_lst)
        # return main_lst
        