class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
            1. Basically I need to count the frequency of item in the array
                1a. can be done easy by using counter
                1b. HashMap, key as items and frequency as value   
            2. Return top frequencies specified by k
                2a. Top: means we need to sort the frequencies (frequencies are values)
                    2b. BUT WE NEED TO RETURN KEYS not values
                2c: So, sort the entire hashMap by values
                2d: return Top K from the sorted HashMap
        '''
        res = defaultdict(int)

    # 1
        for i in nums:
            res[i] += 1
    
    # 2
        buckets = [[] for _ in range(len(nums) + 1)] # need range() + 1 as freq can be equal to len(nums)
        for key, v in res.items():
            buckets[v].append(key)
        
        res_2 = []

        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res_2.append(num)
                if k == len(res_2):
                    return res_2