class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        count = 0
        while l<=r:
            left = limit - people[r]
            r-=1
            count+=1
            if l<=r and left>=people[l]:
                l+=1
        return count

        