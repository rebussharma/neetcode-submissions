from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            days_used = 1
            current_load = 0
            
            for w in weights:
                if current_load + w > capacity:
                    days_used += 1
                    current_load = 0
                current_load += w
            
            return days_used <= days
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            if can_ship(mid):
                right = mid  # try smaller capacity
            else:
                left = mid + 1  # need larger capacity
        
        return left