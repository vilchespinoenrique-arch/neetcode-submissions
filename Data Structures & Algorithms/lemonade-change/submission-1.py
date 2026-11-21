class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        

        if bills[0] != 5: 

            return False 


        # for this we need to think of the possible scenarios 


        # we get: 

        # 5 -> count it, is ours 

        # 10 -> receive it, and subtract one from 5 

        # 20 -> we dont have to keep count of this, we would only subtract either  10 and 5, or 5 5 5 


        five = 0 

        ten = 0 


        for x in bills: 

            if x == 5: 

                five += 1 

            
            elif x == 10: 

                ten += 1 

                if five == 0:

                    return False 

                else: 

                    five -= 1 


            else: 

                if ten == 0: 

                    if five >= 3:

                        five -= 3 

                    else: 

                        return False 

                else:

                    if five >= 1:

                        five -=1 

                        ten -= 1 

                    else: 

                        return False
        
        return True 


        