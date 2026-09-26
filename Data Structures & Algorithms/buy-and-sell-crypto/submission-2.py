class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # the price of the array is price of the coint that day

        # for example, if we have:

        # Input: prices = [10,1,5,6,7,1], the prices will be

        # 10 in day 1, 1, in day 2, and so on and on 

        # we can use 2 pointer for thsi question, where we move along to the right with the 2 pointer,

        # so we set a pointer to be i, and the other i + 1, so that we can check the one to the right 
        best = 0
        i = 0
        

        
        for i in range(0, len(prices)):
            j = i + 1

            while j < len(prices):# while prive 10 is smaller, then we can keep going
                
                difference_of_prices = prices[j] - prices[i] 
                best = max(best,difference_of_prices)
                j = j + 1

        # lets check if this works. 
        return best 


            
                