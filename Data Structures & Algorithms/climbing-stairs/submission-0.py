class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 0
        if n > 0:
            one, two = 1,1
        for i in range(n):
            tmp = one
            one = one + two
            two = tmp
            print(one, two)
        return two