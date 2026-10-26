class Solution:
    def arrangeCoins(self, n: int) -> int:


        # this question has math involved. so we are being asked to find the biggest cantity of complete rows that we can create starting from 1

        # the thing is that we have 1, then that will get increaso to 2, then 3, then 4 and so on 


        # example: 

        # 1 + 2 + 3 + 4 + 5 + 6


        # there is a trick k = k * ( k + 1) / 2 

        # but what is that trick representing really?. the main idea is that we want to create a perfect square so that we dont have to add everything 1 by 1 which would make everything super annonying 

        # like think about the example 


        #  0 
        #  0  0
        #  0  0  0
        #  0  0  0  0
        #  0  0  0  0  0
        #  0  0  0  0  0  0  

        # now thing about this for a second what do you rather do. add that 1 by one... or make this a perfect square??? 

        # obviously make it a perfect square, look at this. 

        #  0  x  x  x  x  x  x
        #  0  0  x  x  x  x  x
        #  0  0  0  x  x  x  x
        #  0  0  0  0  x  x  x
        #  0  0  0  0  0  x  x
        #  0  0  0  0  0  0  x

        # you see how that is just the same thing but only backward!!!! isnt that crazy so we would do 

        # 7 x 6. which is 42 and then we didvide that by 2 which is 21. 

        # so the final total number is 21. 


        # which is prettu cool and that is represented as 


        # k(k + 1) // 2 


        # okay so we are told that n = 4. this is the amount of coints that we have so we need to know how many rows we can achieven and for that we use the formula 

        # coints_need = k ( k + 1 ) // 2 


        # here we are going to use k as mid, because it will be a representaion on what it can be, so that we know how clsoe we are     


        left = 0 

        right = n

        bigger = 0



        while left <= right: 


            mid = (left + right) // 2 



            coints_needed = mid * (mid + 1) // 2  



            if coints_needed <= n:

                bigger = mid 

                left = mid + 1

            
            else: 

                right = mid - 1 



        return bigger  


    



        

           

        

        