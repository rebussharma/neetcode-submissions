class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        '''
            Input: nums = [2,4,10,1,5], k = 2 Output: 16
            Basically we need it split this array nums into K parts
                and return the lowest MAX sum from them
            [2,4,10,1,5]
                can be split in two parts as:
                [2,4,10,1,5] [] = max sum 22
                [2], [4,10,1,5] = Here max sum is 20
                [2,4] [10,1,5] = Here max sum is 16
                [2,4,10] [1,5] = max sum 16
                [2,4,10,1] [5] = max sum 17
            So, we return 16 as result
        '''
        '''
            It is clear from example above that
                1. the max element in arr [10] can be (or is part of) the lowest MAX SUM
                2. the sum of entire array will be the HIGHEST max sum
            These are our range. Now all we do is:
                1. do binary search in range 10 - 22
                2. loop in the original array
                3. assign result as long as mid <= lowest MAX sum
        '''
        def canSplit(largest):
            subArray = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest: # if curresnt sum is exceeding our mid value, then we need a new subArray
                    subArray += 1
                    curSum = n # since adding n made our curSum larger than mid,
                                # we started a new subArray
                                # and the n should be part of newSubArray
            return subArray <= k

        l = max(nums)
        r = sum(nums)
        res = r

        while l <= r:
            mid = l + (r-l)//2

            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
