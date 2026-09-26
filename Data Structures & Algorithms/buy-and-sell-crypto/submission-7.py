class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        best = 0 


        i = 0 
        
        j = 1 

        while j < len(prices): 

        

            if prices[i] < prices[j]: 
                
                

                best = max(best, prices[j] - prices[i])

                j = j + 1


            else: 

                i = i + 1

                j = i 

                j = j + 1

        
        return best





    