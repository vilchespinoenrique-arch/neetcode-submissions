class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        

        # notice that the last number and the first number will always be the biggest ones, so compare them and then add it 


        left = 0 

        right = len(nums) - 1 

        new_list = [0] * len(nums)

        position = len(nums) - 1

        while left <= right: 


            if nums[left] ** 2 > nums[right] ** 2:

                
                new_list[position] = nums[left] ** 2

                position -= 1


                left += 1 

            
            else: 
                
                new_list[position] = nums[right] ** 2

                position -= 1

                right -= 1 

        
    


        return new_list 