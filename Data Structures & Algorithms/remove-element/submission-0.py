class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # in order to remove an element the easiest way if to use a value that will count where we are exactly 

        k = 0 

        for i in range(len(nums)):
            if nums[i] != val: 

                nums[k] = nums[i] # so the first on is val, so this wont apply
                # we will move to the enxt one. same thing, since they are equal we will just keep going
                # now when we get to the 2, that is not the same as 1. so we will take that one, and put at the start of our indes

                # nums[0] = 2, and it will be the first one of our list and so on and on ,

                k = k + 1


        return k

            
        