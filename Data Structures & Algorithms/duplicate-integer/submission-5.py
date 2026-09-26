class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) != len(set(nums)):
            return True # because there are duplicates 
        else: 
            return False
            
        