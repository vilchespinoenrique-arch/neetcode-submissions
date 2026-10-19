class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        

        # the firs thing i would do is sort the numbers


        new_sum = nums.sort()


        left = 0 

        right = len(nums) - 1 

        # [1, 8, 23, 24, 33, 34, 54, 75]

        best = 0 

        while left < right: 


            total = nums[left] + nums[right]
            
            if total < k: # if the total is smaller than k, it means that we need to move the left side only 


                left += 1

                best = max(best, total)


            
            elif total >= k: # whenever that total is bigger 

                right -= 1 

            
        

        if best:     
            return best

        else: 

            return -1





        # [34,23,1,24,75,33,54,8]

        # [1, 8, 23, 24, 33, 34, 54, 75]


            