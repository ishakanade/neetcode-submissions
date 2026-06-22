class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute force
        # hashmap instead of 2 for loops
        # sort and return middle element
        # Boyer Moore algorithm - maintain a cadidate, 
        # whenever there is a opponent reduce the count else 
        # increment it return the candidate at last

        count = 0
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    
            