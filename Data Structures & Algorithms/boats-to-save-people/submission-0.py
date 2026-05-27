class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        if not people:
            return res
        
        people.sort()
        l, r = 0, len(people) - 1

        while l <= r:
            if l == r:
                res += 1
                break
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
        return res