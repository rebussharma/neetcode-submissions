class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
             
            [1,3,4,2,2]
            index   0   1   2   3   4
            n       1   3   4   2   2
            Questio says each integr is in range 1-4
                so integer at index 0 is head, it will not be a part of cycle
                This is important as when we detect cycle we say cycle is there
                    where both slow and fast pointer meet
                But slow and fast actually meet at head first, hence head has to be excluded

            if we consider every value as a pointer,
            each value will point to some index
                n = 1 meaning it points to index 1 with val 3
                n = 3 meaning it points to index 3 with val 2
                n = 4 points at index 4 with val 2
                n = 2 points at index 2 with val 4
                n = 2 points at index 2 with val 4 again

        '''
        s, f = 0, 0

        while True:
            s = nums[s] # slow points to nums slow
            f = nums[nums[f]] # advancing fast twice
            if s == f:
                break

        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s        