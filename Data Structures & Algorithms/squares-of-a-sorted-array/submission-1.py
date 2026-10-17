class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        new_list = []

        for i in range(0, len(nums)): 

            new_list.append(nums[i] * nums[i])


        new_list.sort()


        return new_list