class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return -1

        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            singleJump = cost[i] + cost[i+1]
            doubleJump = cost[i] + cost [i+2]
            cost[i] = min(singleJump, doubleJump)

        return min(cost[0], cost[1])