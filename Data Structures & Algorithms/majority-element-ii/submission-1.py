class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2: # if our hashMap still has space
                continue 
            # if our hashmap has more than 2 elements
            new_map = defaultdict(int)
            for n, c in count.items(): # O(1) for this loop iteration as count has fixed length
                  if c > 1: # this way we do NOT add new elements with freq 1 to new count
                       new_map[n] = c - 1
                       """
                        Might confuse us but lets take [0,0,3,3,4,4,4] for example
                        arr lenght = 7, top freq must have freq of GREATER tha 2 (7//3).
                        Only 4 has freq greater than 2

                        n:      countmap               countmap lenght
                        0:      {0:1}                   1 
                        0:      {0:2}                   1
                        3:      {0:2, 3:1}              2
                        3:      {0:2, 3:2}              2
                        4:      {0:2, 3:1, {4:1}        3

                        Now we have surpassed max element (2), so need to remove an element
                        1. We cannot just remove the element with lowest freq (4) as later we might have tons of 4
                        2. So we just copy all elements inot a new map
                            but leave out element whose frequency is NOT greater that 1
                            but we also need to reduce freq of all remaining items in new map by 1
                                this is so that if later we see more 4, 4 takes space of remaining item
                        new_map

                       """
            count = new_map

        res = []

        # for loop below with nested if has TC of O(n)
        for n in count: # this is O(1) as we only have 2 elements max in count
             if nums.count(n) > len(nums) // 3: # this is O(n)
                  res.append(n)
        return res