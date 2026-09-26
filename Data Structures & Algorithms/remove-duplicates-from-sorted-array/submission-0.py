class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 


        for j in range(1, len(nums)): 

            if nums[i] != nums[j]: # if they are not equal, then go ahead and and added to the arr 

                i += 1 

                nums[i] = nums[j]


        return i + 1