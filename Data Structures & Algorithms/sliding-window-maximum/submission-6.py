class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # dq will store INDICES of elements (not values)
        # IMPORTANT: values at these indices will be in DECREASING order
        dq = deque()

        # This will store the final result (max of each window)
        res = []

        # Loop through each element with index and value
        for i, num in enumerate(nums):

            # ---------------------------------------------------
            # STEP 1: Remove all elements from the BACK of deque
            #         that are smaller than the current element
            # ---------------------------------------------------
            # WHY?
            # Because if current number is bigger, smaller ones
            # will NEVER be useful again (they can’t be max)
            #
            # Example:
            # dq has indices of values [5, 3]
            # new number = 6
            # → 5 and 3 are useless → remove both
            #
            while dq and nums[dq[-1]] <= num:
                dq.pop()  # remove from BACK


            # ---------------------------------------------------
            # STEP 2: Add current index to the BACK of deque
            # ---------------------------------------------------
            # We store index instead of value so we can:
            # - Check if it's out of window later
            dq.append(i)


            # ---------------------------------------------------
            # STEP 3: Remove element from FRONT if it's OUTSIDE window
            # ---------------------------------------------------
            # Current window = [i-k+1 ... i]
            #
            # So anything <= (i - k) is OUTSIDE the window
            #
            # Example:
            # i = 4, k = 3 → window = [2,3,4]
            # so index 1 is invalid → remove it
            #
            if dq[0] <= i - k:
                dq.popleft()  # remove from FRONT


            # ---------------------------------------------------
            # STEP 4: Add result when window is FULL
            # ---------------------------------------------------
            # First valid window is when i >= k - 1
            #
            # The MAX element is ALWAYS at the FRONT of deque
            #
            # WHY?
            # Because:
            # - smaller elements were removed earlier
            # - front always holds the largest valid element
            #
            if i >= k - 1:
                res.append(nums[dq[0]])


        # Return final result list
        return res