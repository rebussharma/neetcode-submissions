class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in (asteroids):
            while res and res[-1] > 0 and a < 0:
                if abs(res[-1]) < abs(a):
                    res.pop()          # top explodes, keep checking
                    continue
                elif abs(res[-1]) == abs(a):
                    res.pop()          # both explode
                break                    # current asteroid dies
            else:
                res.append(a)          # no collision → survives
        
        return res