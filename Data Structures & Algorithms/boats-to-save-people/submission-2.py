class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boats = 0
        while l<=r:
            curr_weight = people[l]+people[r]
            if curr_weight > limit:
                r-=1
            else:
                l+=1
                r-=1
            boats+=1
        return boats