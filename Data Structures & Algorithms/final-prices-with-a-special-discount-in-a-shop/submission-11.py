class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pass


        # the way i will do this is by using 2 pointer, if the value that comes next is smaller then i will aply the discount and append it. 


        # if the value is bigger i will increase the other pointer until i cant no more, and if there isnt anything else, then  i would append that first one 


        i = 0 

        j = 1 

        result = []


        while i < len(prices): 
            
            if j == len(prices): 

                result.append(prices[i])

                i += 1

                j = i + 1 
            
            
            elif prices[i] < prices[j]:

                j += 1 
                

            

            else: 

                result.append(prices[i] - prices[j])
                
                i += 1

                j = i + 1 

        
        return result 



            
            

            


                    

                
