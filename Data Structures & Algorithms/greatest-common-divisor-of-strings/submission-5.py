from math import gcd 

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        

   
            # the really cool thing about this problem is that we can use something that is called gmd, with this we can get the bigger divisble number, let me give you an example of what it would give us 




            # a = 32    ,   b  = 16 


            # the function would take this and give the biggest divisor which is 8. 


            # and that is exactly what we need for this question, the biggest divisor between those 2 strings and with that we can return what we want 


            if str1 + str2 !=  str2 + str1: 

                return ""

            
            lenght1 = len(str1) 

            lenght2 = len(str2) 


            biggest_divisible = gcd(lenght1, lenght2)



            return str1[:biggest_divisible]



