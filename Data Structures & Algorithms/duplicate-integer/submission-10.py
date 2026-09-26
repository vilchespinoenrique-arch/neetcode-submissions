class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        # for this quesiton if we use a set the asnwer will be o 1 




        # sets will only take real unique values, knowing this we can asnwer the question 


        new_nums = set(nums) # we just put the nums in the set 


        if len(new_nums) != len(nums): 

            return True 


        else: 

            return False 