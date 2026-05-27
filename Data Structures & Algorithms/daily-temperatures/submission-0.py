class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        ms = []

        for i, t in enumerate(temperatures):
            while ms and t > ms[-1][1]:
                res[ms[-1][0]] = i - ms[-1][0]
                ms.pop()
            ms.append([i, t])
        return res