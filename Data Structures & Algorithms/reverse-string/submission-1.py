class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # this question is really good for the two pointer rule, the reason I say this is becasue we can use the two pointer and just modify
        # as we do the movement 

        left = 0 
        right = len(s) - 1
         
        while left < right: 

            s[left], s[right] = s[right], s[left]  # this is going to make 
          
            #  we have to do it at the same time, becasue otherwsie, we can modify values if we do one first and then the other 

            # they will be chaning until they meet in the middle 

            left += 1 
            right -= 1 

