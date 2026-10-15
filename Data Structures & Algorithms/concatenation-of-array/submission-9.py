class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:


        result = []



        while len(result) != len(nums) * 2: 


            for num in nums: 

                result.append(num)


        return result 
        