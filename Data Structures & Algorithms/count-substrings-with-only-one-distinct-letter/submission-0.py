class Solution:
    def countLetters(self, s: str) -> int:

        # there is a patter in this question that is hard to find but, if you look closely, you can see that whenever we have repeating characters it would ended up being like this: 


        # aaa -> this is the same as 3 + 2 + 1 , which is the same as lenght  + length - 1, length - 2... 


        # which is what we watn to do 


       

        # i will use hold to hold the current numbers that are equal so that i can count the 


        run = 0 

        total = 0


        for i in range(0, len(s)):


            if i > 0 and s[i] == s[i - 1]: 

                run = run + 1 

                # if they are the same we are going to add the run to +1, and then we will keep adding that as long as they remain the same, if they dont we will reset run to 1


            else: 

                run = 1 


            total = total + run 



        return total  



            


                