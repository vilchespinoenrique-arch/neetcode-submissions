class Solution:
    def isArmstrong(self, n: int) -> bool:
        


        new_n = str(n)

        length = len(new_n)

        total = 0

        for number in new_n: 


            # right now lets look at each number 

            num_again = int(number)

            total = total + num_again**length

        
        if total == n: 

            return True 

        else: 

            return False 