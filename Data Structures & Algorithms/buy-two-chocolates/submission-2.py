import heapq

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        

        # gets the top 2 smalles values, and for this we can use a heap 


        heap = [] 


        for x in prices: 

            heapq.heappush(heap, -x) 


            if len(heap) > 2: 

                heapq.heappop(heap) 


    
        # now in the heap we have 2 of the smaller values 


        x = -heapq.heappop(heap) 


        y = -heapq.heappop(heap)


        combination = x + y 

        result = money - combination 


        if result >= 0: 

            return result 

        else: 

            return money 
