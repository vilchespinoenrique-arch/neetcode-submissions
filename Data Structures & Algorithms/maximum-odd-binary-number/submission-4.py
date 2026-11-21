class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:


        one = s.count("1")


        zero = len(s) - one 



        new_string = ""


        for _ in range(one - 1): 

            new_string += "1" 
        

        for _ in range(zero): 

            new_string += "0"


        new_string += "1" 


        return new_string  
        