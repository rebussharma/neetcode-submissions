class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ''' 
            1. for list [1,1,2,2,3,4,4]
                a. take first element 1 at index 0
                b. this is a duplicate of 1 at index 1

            2. So, to find duplicate 
                a. take a number, store into a variable (prev)
                b. compare prev number to next number
                    If not equal then they are not duplciate
                c. Iterate over the input list, while updating prev value

            3. Since input is sorted, duplicate will be next to each other.
                a. i.e [1,1,2,2,3,4,4] this is guranteed
                b. we won't get input like [1,2,1 as] this list is NOT sorted
                c. we also need to modify the array in place
                    ca. so, we will append unique numbers to list
                    cb. at the end, we will just return total numbers appened.
                        cba. you can do this in python by assigning input list to values AFTER append
                        cbb. or just use a counter and do counter ++ whenever there's append
                
        '''
        starting_length = len(nums)
        prev = nums[0]
        nums.append(prev) # append first number as it doesn't have a duplciate (yet)
        for i in range(1, starting_length):
            if nums[i] != prev:
                nums.append(nums[i])
            prev = nums[i]
        del nums[:starting_length] # this line will delete all values from nums that are before starting lenght
        return len(nums)