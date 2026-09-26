class Solution:
    def validPalindrome(self, s: str) -> bool:
        # something very useful that i didnt know is that when we do [::-1] we literally get the word backwards, which i think is really cool and i didnt know this before 

      # firs thing we do a check for left and right, and if they are equal we just keep moving along

      left = 0
      right = len(s) - 1 


      while left < right:
        
        if s[left] == s[right]:

            left += 1 
            right -= 1 

        # if they are equal go ahead and add and subtrac so that we can keep on checking

        else: 
            # if we find something that doesnt match, we will do the following: 

            erase_left = s[left+1 : right + 1] # this will give us a slicing, when we eliminate that left side, we will check for that 

            # lets say we have the value: ABBDA

            # THE FIRST will go so we will the have
            # bbd left 

            #  left = 1
            # right = 3 

            # erase_left = s[2 : 4]
            # so it will go from index 2 - 4.. it will finish in 3 and consider 3 

            # ABBDA # INDEX 2 = b INDEX 3: D 

            # so it will return "BD"

            erase_right = s[left:right] # this erases the right part instead, and we will see why 

            # erase right will return 
            # left = 1
            # right = 3 

            # s[1:3] so it will finish in the 2 index 

            # ABBDA -> "BB"
            
            
            return erase_left == erase_left[::-1] or erase_right == erase_right[::-1]
            # if either is true it will return true.. then we can keep on going 

            #  NOW Lets check is "BD" == "DB" are they palindrom? they are not so that is false 

            # is "bb" == "bb"? yes that is a palindrome. 

            # since we have a false and a true, we return true, becasue one of them was true 
    
      return True # if we finish the loop we also return true 