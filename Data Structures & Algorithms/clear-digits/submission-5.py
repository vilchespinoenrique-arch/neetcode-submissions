class Solution:
    def clearDigits(self, s: str) -> str:
        pass


        # for this question is important to know this functions 

        # isdigit() -> if is a digit 

        # isalpha() -> if is a letter 

        if len(s) == 1: 

            return s 


        stack = [] 


        for char in s: 

            if stack and stack[-1].isalpha() and char.isdigit():

                stack.pop()

            else: 

                stack.append(char)

        
        return "".join(stack)


        