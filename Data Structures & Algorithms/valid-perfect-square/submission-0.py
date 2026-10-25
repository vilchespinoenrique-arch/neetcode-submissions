class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        

        # for this question i think a good idea would be you keep diving the number till you find the right fit for 

        # mid * mid = num 


        left = 0 

        right = num 

        # lets follow an example with 9, becasue i think that is a hard perfect square to have 

        while left <= right: 

            mid = (left + right) // 2 

            # for now if we where doing 9, that would be 4. 

            if mid * mid == num: 

                return True  

            elif mid * mid > num: # if the mid is bigger it means that we have to go a litle bit smaller 

                right = mid - 1

            else: # where the mid is smaller

                left = mid + 1 


        return False