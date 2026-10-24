class Solution:
    def makeGood(self, s: str) -> str:
        pass


        if len(s) == 1: 

            return s 

        
        # for this question what im thinking of doing is to replace the letter after if they have a match, however i need to know how to indentify capital letter,


        # the way you would do that you do it in 2 ways 

        # so first you need to ask if the letter are different becasue a and A are different and they get treated diferrently 


        # then after you check for that you would check if current.lower() == next.lower(), and if that is true and that they are different is true then you can pop them 


        # what im thinking for this question is grabbing the letter of s, and as they keep coming comparing them, and if they dont match the last one i added then keep adding them, but if they do then go ahead and pop them 


        stack = []

        for char in s: 




            if not stack or char.lower() != stack[-1].lower() or stack[-1] == char: 


                stack.append(char)

            
            elif char != stack[-1] and char.lower() == stack[-1].lower():

                stack.pop()

        
        return "".join(stack) 



        