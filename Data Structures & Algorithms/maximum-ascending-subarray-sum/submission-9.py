class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        

        total_increase = nums[0]

        biggest_total_increase = nums[0]


        for i in range(len(nums) - 1): 



            if nums[i] < nums[i + 1]: 

                total_increase = total_increase + nums[i + 1]
                


            else: 

                total_increase = nums[i + 1] 


            biggest_total_increase = max(biggest_total_increase, total_increase)


            


        return biggest_total_increase
            

