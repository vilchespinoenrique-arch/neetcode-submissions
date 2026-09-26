class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        # why we are being asked in this question is that we need to do a regular binary tree, and then they want us to get what would be the next number 


        left = 0 

        right = len(nums) - 1 


        while left <= right: 

            mid = (right + left) // 2


            if nums[mid] == target: 
                return mid 


            elif nums[mid] > target: 

                right = mid - 1 # if the current number is bigger, it means that the target will be in the smaller numbers 

            else: 

                left = mid + 1 


        return left 

        # now lets see why returning left is the reason why we get the answer that would be there 


        # Input: nums = [-1,0,2,4,6,8] , target = 5 

        
        #  mid = 2 

        # left = 3

        # mid = 4 

        # right = 5

        # then we have [4,6,8]

        # 6 > 5. so we make right = 4 - 1 = 3 

        #  3 + 3 = 6 // 2 = 3 


        # mid = 3 

        # 4 is the mid now, so we only have [4] 

        # and since target = 5, and 5 > 4, then we have to make another conversion 

        # left = 3 + 1 = 4 

        # and now if we didnt find the asnwer, we would know that the next one will always be the biggest one after the one we had, which would be left 

        # and  

        



