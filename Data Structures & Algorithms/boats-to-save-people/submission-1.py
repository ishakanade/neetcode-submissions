class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # [1,2,4,5,6]
        # [12233]
        i = 0
        j = len(people)-1
        boat_count = 0
        while i<=j:
            if people[i] + people[j] <= limit:
                i+=1
            boat_count +=1
            j-=1
        return boat_count