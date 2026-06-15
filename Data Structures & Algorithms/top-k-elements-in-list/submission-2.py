class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1+ count.get(i, 0)
        for num, count in count.items():
            freq[count].append(num)
        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result)==k:
                    return result


        # O(nlogn)
        # numsdict = defaultdict(list)
        # for i in nums:
        #     numsdict[i] = 1 + numsdict.get(i,0)
        # value_dict = sorted(numsdict.items(), key=lambda i: (i[1], i[0]))
        # if len(value_dict) < 2:
        #     return ([key for key, _ in value_dict])
        # else:
        #     return ([key for key, _ in value_dict[-k:]])
        