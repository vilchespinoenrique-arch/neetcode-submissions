class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pass

        i = 0 


        j = 1 


        discount = 0

        result = []



        while i < len(prices): 

            if j == len(prices): 

                result.append(prices[i])

                i += 1 

                j = i + 1

            elif prices[i] < prices[j]:
                

                    j += 1

       

            else: 


                discount = prices[i] - prices[j]


                result.append(discount)


                i += 1 

                j = i + 1 


        return result 
