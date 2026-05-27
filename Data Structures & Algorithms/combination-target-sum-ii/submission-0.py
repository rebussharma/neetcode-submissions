class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def bt(i, ss, total): 
            if total == target:
                res.append(ss.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # include nums[i]
            ss.append(candidates[i])
            bt(i+1, ss, total + candidates[i])

            # do not include nums[i]
            ss.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            bt(i+1, ss, total)
        bt(0, [], 0)
        return res