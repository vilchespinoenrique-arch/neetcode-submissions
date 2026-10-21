class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        pass

        left = 0 


        right = 1





        while right < len(nums): 


            if nums[left] == nums[right]: 

                nums[left] =  nums[left] * 2

                nums[right] = 0


            left += 1

            right += 1


        nums.sort(key=lambda n: n==0)


        return nums



       

        

            
          
          



