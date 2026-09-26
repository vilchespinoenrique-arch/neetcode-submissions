class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        

        # what we want to do for this quesiton is we want to go throught the array and we want to have

        # a left side which would be the add one of the numbers that we have pass, and we also want a right side

        # whihc would be the total of the numbers that we have - the left side - the current index, becasue we dont count that



        # so it look something like this: 


        # left side = left side + nums[i] 



        # right side = total - left_side - nums[i]
        #  - nums[i] representing the number that we are currently in 




        left_side = 0 
        left = 0

        total = sum(nums) # the total would alway remain the same 


        for i in range(len(nums)): 

            left_side = left_side + left 
            
            left = nums[i]

            right_side = total - left_side - nums[i]


            if left_side == right_side: 

                return i

        return -1

            

        
            