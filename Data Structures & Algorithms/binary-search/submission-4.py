class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # a key thing to look here is that they want o log n. that means that it could be binrary tree or binary seatch. it could be other things but those are the most likely honestly 


        # we have nums = [-1, 0 , 2, 4, 6, 8]


    
        length = len(nums)

        left = 0 

        right = length - 1 





        while left <= right: 


            middle = (left + right) // 2 




            if nums[middle] == target: 


                return middle 


            elif nums[middle] < target: 


                left = middle + 1


            else: 

                right = middle - 1 
        

        return -1 