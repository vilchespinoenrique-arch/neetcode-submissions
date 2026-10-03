class Solution:
    def arraySign(self, nums: List[int]) -> int:
        

        # count how many negatives number there are, if its even it means that we will get a positive, if odd, it means we will get an odd number. if theree is even 1 zero it means we will get 0

        negatives = 0

        for num in nums: 

            if num == 0: 

                return 0 

            elif num < 0: # if num is negative 


                negatives += 1 



        if negatives % 2 == 0:  

            # if is even then return 1 
            return 1 

        else: 

            return -1

