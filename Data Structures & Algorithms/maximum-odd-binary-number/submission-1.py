class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        

        ones = s.count("1")

        zero = len(s) - ones



       # now we know the total for the ones and the total for the zeroes 

        new_string = ""

        for _ in range(ones - 1):

            new_string += "1" 


        for _ in range(zero): 


            new_string += "0"


        new_string += "1"


        return new_string 