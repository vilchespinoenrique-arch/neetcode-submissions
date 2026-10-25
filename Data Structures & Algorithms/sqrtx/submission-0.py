class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:

            return x 
        # this quesiton is pretty weird, but we want to use a binary search to find the answer. the reason why we want to do that is becasue 


        # we have for example 16 

        # we know that the square root of 16 has multiples answers


        # 16 = 


        # [2, 4, 8]  the possible answer can only be aroung this. if its not for that it cannot be anywhere else,

        # nothing else makes sense, those are the 3 solutions 


        left = 2 

        right = x // 2  #this is the other option we have for the right side 


        # we are keeping all the possiblities that it could be 

        # [2, 4, 8] 


        # now we just do a normal binary search 

        while left <= right:

            mid = (left + right) // 2 

            num = mid * mid # if we get the mid * mid == to the number, that means that is our square root 
            
            
            if num == x:

                return mid 

            elif num > x: # if the number is bigger thant the number, then we have to get a smaller value 

                right = mid - 1 

            else: 

                left = mid + 1 
        
        return right  


        # lets look an examle so that we can see how returning right gives us the naroowing down part 

        # 8 

        # left = 2

        # right = 4 

        # [2, 4] 

        # the mid is 3

        # 3 * 3 = 9 

        # this is bigger, so we need to make our right smaller 

        # right = mid - 1 = right = 3 - 1 = 2 

        # now we have 

        # right = 2

        # left = 2 

        # the mid of this is 2 

        # 2 * 2 = 4 

        # since 4 is to low so now left become 

        # left = mid + 1 = left = 4 + 1 = 5 

        # now we have left = 5 

        # right = 2

        # this breaks the while loop and we stay we are closest number which was right 
             



