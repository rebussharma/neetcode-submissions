class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            backtracking(i, cur, total + nums[i])

            cur.pop()
            backtracking(i+1, cur, total)
    
        backtracking(0, [], 0)
        return res