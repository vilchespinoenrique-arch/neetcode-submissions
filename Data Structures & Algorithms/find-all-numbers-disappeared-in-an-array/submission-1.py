class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:


        seen = set() 

        n = len(nums)

        result = []

      # make sure that we have all of the numbers in the set first 


        for i in range(n): 


            seen.add(nums[i]) 

        # this would look like this: 

        # seen = { 4, 3, 2, 7, 8, 2, 3, 1}

        for i in range(1, n + 1): 

            if i not in seen: 

                result.append(i)


        # so we would go throught the whole thing, and then we will look for the numbers that we have not seen in here

        # and then 
        return result 

      