class Solution:
    def isUgly(self, n: int) -> bool:
        

        # in order for the quesiton to be ugly we would need to get the number to becomes  1, if the number reaches 1, it means that is an ugly number

        if n == 1: 

            return True 

        while n % 2 == 0: 
            
            n = n // 2 

            if n == 1: 

                return True 

        while n % 3 == 0: 

            n = n // 3 
                
            if n == 1: 

                return True 


        while n % 5 == 0: 

            n = n // 5

            if n == 1: 

                return True 


        return False


