class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(set(nums)) != len(nums):

            return True 


        # this is saying that if the numbers [1, 2, 3, 3] 

        # for example this numbers in a set would tranform like this 


        # {1, 2, 3} and it would only keep the ones that are no duplicates, so the originals ones 


        # if you notice that the amount in that set is not the same as the one that you started with, it means that there has been a change meaning that there was a duplicate. 

    # so in that case we would return true 


        else: 

            return False 