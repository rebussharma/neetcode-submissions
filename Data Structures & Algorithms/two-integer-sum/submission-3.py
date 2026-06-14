class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        '''
            3,4,5,6     10


            hs = {}

            3
                check if diff is in hs:
                    hs[3]: index

            4
                hs {3:0, }
                check if diff (6) in hs:
                updates hs

            5
                hs {3:0, 4:1,5:1}



            6
                    return index, hs[diff]

        '''

        hs = defaultdict(int)

        for i, v in enumerate(nums):
            diff = target - v
            if diff in hs:
                return [hs[diff], i]
            hs[v] = i

        return []