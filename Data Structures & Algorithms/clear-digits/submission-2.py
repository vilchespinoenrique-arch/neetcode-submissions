class Solution:
    def clearDigits(self, s: str) -> str:
        pass

        # for this question is good to remeber the functions: 

        # isalpha() -> meaning is a letter

        # isdigit() -> meaning is a number 



        if len(s) == 1: 

            return s 

        stack = [] 


        for char in s: 
            
            if stack and stack[-1].isalpha() and char.isdigit():

                stack.pop()

            
            else: 

                stack.append(char)


        return "".join(stack)