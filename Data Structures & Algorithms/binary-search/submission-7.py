class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # a key thing to look here is that they want o log n. that means that it could be binrary tree or binary seatch. it could be other things but those are the most likely honestly 


        # we have nums = [-1, 0 , 2, 4, 6, 8]


        # notice also that they are in order so that makes it easier to use the know strategic that is binaary search 


        # the idea of bindary search is. it will look at middle number and it will see if that number is the target the are looking for, or if its bigger or smaller. and accoridng to that asnwer it will cut the array in half and repeat the process. 



        length = len(nums)

        left = 0 

        right = length - 1 



        # now to define the middle. the middle will be different depending on where we are so the midlle will always be changing, well so that middle, right and left 


        while left <= right: 

            # so while the right side is bigger than the left side, it should be ok and we can keep going 

            middle = (left + right) // 2 

            # we use // becasue that will give the division to finish in a base number, so if we get 1.5 it would be 1. that way we dont get the middle 


            if nums[middle] == target: 

                return middle 


            elif nums[middle] > target: 

                right = middle - 1 



            else: # this would mean that the target is bigger than the answer we got. 

                left = left + 1
        

        return -1

