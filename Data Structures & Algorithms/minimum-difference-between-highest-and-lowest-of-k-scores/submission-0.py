class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        

        # for this question we want to sort the number, and after we sort he nuber so that we can have the closer number togetherts

        # nums = [9, 4, 1, 7], k = 2, use this as your example. the most important thing here, 

        # is to keep in mind of our window. the way we will do that is by 


        # using i + k - 1  

        # think about it i + k - 1, will away be withing the window distance, which is exactly what we want 

        nums.sort()

        min_difference = 1000000

        # [1, 4, 7, 9]

        for i in range(len(nums) - k + 1): # this will make us finish just when we have the last index for that window

            current_difference = nums[i + k - 1] - nums[i] 


            min_difference = min(current_difference, min_difference)

                # this will be 1 - 4 = 3  

                # then it will be 

                # 4 - 7 = 3 

        return min_difference

