class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        

        
        

        for i in range(len(nums)): 


            if nums[i] % 2 == 0: 

                nums[i] = 2 # 2 here will represent even


            elif nums[i] % 2 != 0: 

                nums[i] = 1  # 1  here will represent odd 


        
        # at the end i will have a modified list 


        # nums = [2, 1, 1, 2] 


        for i in range(len(nums) -1 ): 


            if nums[i] == 2: 

                if nums[i + 1] == 2: 

                    return False
                
                else: 
                    continue 

            elif nums[i] == 1:

                if nums[i + 1] == 1:
                    
                    return False 

                else: 

                    continue

        return True 


            