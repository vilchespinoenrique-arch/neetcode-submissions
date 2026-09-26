class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        # for this quesiton whast im thinking, is that i should keep a pointer, that points at the index, and another way that goes through the array,

        # and then when i find something, we just move that number that is not a zero to that index 


        index = 0 


        p = 0 

        size = len(nums)


        while p < size: 

            if nums[p] != 0 : 

                nums[index], nums[p] = nums[p], nums[index]
              
                index += 1 
                p += 1 
            
            else: 

                p += 1 


        # nums=[0,0,1,2,0,5] 

        # index = 0, p = 0 

        # while 0 < 6 

            # 0 != 0? no, so we do else, 

            # pointer = 1 
        
        # while 1 < 6 

            # is 0 != 0? 

            # no so pointer =2 

        # while 2 < 6

        # is 1 != 0? yes


        # so we move nums[0] = num[p], which is 1, 

        # so the list look like this right now 

        # [1, 0, 0, 2, 0, 5 ]