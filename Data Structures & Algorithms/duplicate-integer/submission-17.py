class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set num. will always remove the duplicates
        # knowing this we can use that in our favor to check if they are duplicates

        if len(nums) != len(set(nums)):
            return True # if the values is seen more than once return true 

        else: 
            return False 