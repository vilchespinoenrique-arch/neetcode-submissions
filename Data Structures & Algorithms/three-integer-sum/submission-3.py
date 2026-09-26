class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # the idea of this question is to put an i for the numbers and then use 2 other pointers. one for the left and the other one for the right 
        # this way we are able to find any possibilities that will give us 0 

        
        
        

        some_result = []

        nums.sort()

        # the numbers:

        # [-4, -1, -1 0, 1, 2]

        for i in range(len(nums) - 2):

            left = i + 1 
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue # becasue it means that we already used this i 

            # left = 1 
            # i = 0 
            # right = 5

            # [-4, -1, -1 0, 1, 2]

            while left < right: 

                value = nums[i] + nums[left] + nums[right]

                if value == 0: 

                    # value = 3
                    some_result.append([nums[i], nums[left], nums[right]])

                    

                # value = 3

                #handles duplicates 

                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                
                # left being -1 is = -1. so we are good on making left = 2 
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1

                    left = left + 1
                    right = right - 1

                

                
                elif value > 0:
                    right = right - 1
                
                else: 
                    left = left + 1 

        return some_result
                
            
            

            # let check this: 







        