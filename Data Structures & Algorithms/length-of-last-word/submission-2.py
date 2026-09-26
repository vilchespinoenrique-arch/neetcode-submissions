class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # think of the special cases where hello worl for example would have spaces before. 

        # becasue the whole idea is to start from the left and stop whenever we see a space. but make sure

        # that we dont see any spaces before that 


        i = len(s) - 1
        count = 0 


        while i >= 0 and s[i] == ' ': # as long as i is bigger than 0, we can keep on going 

             # if the last letter is equal to a space, then we will continue, and reduce that 

                i -= 1 

        
        while i >= 0 and s[i] != ' ': 

             # if the letter are not a space.. keep on going 

                i -= 1 

                count += 1 

        return count 

