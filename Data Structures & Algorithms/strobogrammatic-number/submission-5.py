class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        # this question is a really weird question and im not even mad that i was not able to answer right away, however the idea for this question is to get the numbers that we know that flipped could be valid numbers. this numbers are 


        # 0, 1, 6, 8, 9 
        

        dictionary = {"0": "0", "1":"1", "6":"9", "8":"8", "9":"6"}


        # now that we have the diccionary we can use it to comapre left side with the right side


        left = 0 

        right = len(num) - 1



        while left <= right: 

            if num[left] in dictionary:
                
                if dictionary[num[left]] != num[right]:

                    return False 
                

                else: 

                    left += 1 

                    right -= 1 


            
            else: 

                return False 

        
        return True 





