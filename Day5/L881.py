"""
Docstring for Day5.L881

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""

class Solution:
    def numRescueBoats(self,people,limit):
        people.sort()
        ans = 0
        l = 0
        r = len(people) -1

        while l<=r:
            x = people[l] + people[r]
            if x<=limit:
                l+=1
                r-=1
            elif x> limit:
                r-=1
            ans+=1
        return ans
people = [3,2,2,1]
limit =3
print(Solution().numRescueBoats(people,limit))


