class Solution:
    def isPalindrome(self, s: str) -> bool:


       

        # so for this example 
        
        # Input: s = "Was it a car or a cat I saw?"


        # the left pointer would point to the left, which is 0, and the right pointer would point to right 



        
        # the first thing we need to do is we need to make the letters to not have capital letters or to not have spaces, so that we dont ran into any problems 


        # for this we can use functions that already in python, so that is good. this ones are easy to remember so we shouldnt have a problem with them 


         
        # new_text = s.lower() 

        # new_text = s.replace(" ", "")

        # new_text = s.replace("")


        # now the new text should have no capital letter and no spaces in between. lets check real quick 


        # i was doing this and i realize something. instead of finding for ways to replace this. actually the best idea is to find what we want. there is also a dunction for this, is called isalnum()


        # now you would be like. that is imposible to remeber. and i would tell you that you are right lol. 


        # but look at this 


        # is -? is 

        # al -> alpha so is it a letter 

        # num -> number 


        # so is saying in the function is this a number or a letter i thoguth that was really cool 


        # it will return true for letter and numbers but flse for naything else 

        new_text = ""


        for char in s: # lets use a loop to go through the letters first and fix them 

            if char.isalnum(): 

                new_text += char.lower() 

                # so this will get only letter and then create a new_text where each character is lower and has no spaces. 


        # now we officialy have the text with no extra things, with no spaces or anything 


        length = len(new_text)

        pointer_left = 0 


        pointer_right = length - 1 



        for _ in range(0, length): 
            
            if new_text[pointer_left] != new_text[pointer_right]: 

                return False 

            else: 

                pointer_left += 1 

                pointer_right -= 1 

        
        return True 
                


