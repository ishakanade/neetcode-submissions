class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = 0
        for i in nums:
            if (i-1) not in nums_set:
                seq_len = 0
                while (i+seq_len) in nums_set:
                    seq_len +=1
                length = max(length, seq_len)
        return length



        