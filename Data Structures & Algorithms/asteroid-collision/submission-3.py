class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in (asteroids):
            res.append(a)
            while len(res) > 1 and res[-1] < 0 and res[-2] > 0:
                if abs(a) < res[-2]:
                    res.pop()
                elif abs(a) == res[-2]:
                    res.pop()
                    res.pop()
                else:
                    res.pop()
                    res.pop()
                    res.append(a)
        return res