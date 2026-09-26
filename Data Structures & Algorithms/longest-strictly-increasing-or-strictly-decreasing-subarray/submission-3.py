class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        

        increasing = 1 
        
        decreasing = 1

        biggest_one_so_far = 1

        for i in range(len(nums) - 1): 

            if nums[i] < nums[i + 1]: 

                increasing += 1 
                decreasing = 1 
            
            elif nums[i] > nums[i + 1]:
                decreasing += 1 
                increasing = 1 

            else: 

                increasing = 1 
                decreasing = 1 


            biggest_one_so_far = max(biggest_one_so_far, increasing, decreasing)


        return biggest_one_so_far

            
        

            
    


            