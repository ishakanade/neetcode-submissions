class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsdict = defaultdict(list)
        for i in nums:
            numsdict[i] = 1 + numsdict.get(i,0)
        value_dict = sorted(numsdict.items(), key=lambda i: (i[1], i[0]))
        if len(value_dict) < 2:
            return ([key for key, _ in value_dict])
        else:
            return ([key for key, _ in value_dict[-k:]])
        
        
        