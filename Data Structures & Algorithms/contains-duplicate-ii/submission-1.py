class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 3 more to go 

        # for this question we want to make sure that we always maintain this same window, which is within  the limits of 3

        # for this example, so if we find one that actually went further, than that, then that means that widnow is not longer valid 


        # let me show you: 

        # also we will keep at index = 0

        # becasue this one will be in charge of knowing where our set erased set was, and we will move it foward, one to erase the next one if necessary


        window = set() 

        i = 0

        for j in range(len(nums)): 

            if j - i > k: # if the windows somehows ends up becoming bigger, then we want to remoce a the last from the window, so that the window can becomes smaller

                window.remove(nums[i]) # we will remove the first elements that we used with window remove  

                i += 1 # increase the 1 for the next one 

            if nums[j] in window:
                
                return True 


            window.add(nums[j]) # make sure that you add the numbers that we are currently using 


        return False 