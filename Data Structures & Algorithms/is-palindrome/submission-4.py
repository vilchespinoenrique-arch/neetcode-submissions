class Solution:
    def isPalindrome(self, s: str) -> bool:


        # lets go part by part. "". join is so that if we have a list, we would join it to 1 thing

        # so for example (h, r, s, t) = hrst 

        # c.lower = makes all the letter into lower case

        # but for now the part that we care about is isalnum, because isalnum is in charge of taking away all the , or the extra things that we dont want 

        # example: "Was it a car or a cat I saw?"

        # it will go one by one 
        # W a s i t a c a r o r a c a t I s a w. so this will clean and get rid of extra spaces and extra things and know we will fine, it will be clean 

        # so we will only keep the true, becasue the ones that are not chatacter it will return false, and we only keep the true 


        # lets see what im taking about 

        # the first step is to make the letter normal 

        new_s = s.lower()

        # now we want to only keep the letters and numbers 

        new_char = []

        for char in new_s:
            if char.isalnum():
                new_char.append(char)

        super_new_char = "".join(new_char) # make the new char into a normal string so that we can compare 
        



        #for this quetion what we want to do is have the idea of two pointers
        # so for one part of the string we will have to star and then on the other side we will be checking for this side 

        left = 0 

        right = len(super_new_char) - 1 # this way it will match perfectly with last one of the string

        #hello - right = 4


        
        while left <= right:

            if super_new_char[left] != super_new_char[right]:
                return False 
            
            else: 
                left = left + 1 
                right = right - 1

            
        return True 

        