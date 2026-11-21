import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        # okay in the question we get hing that we want to use the two heaviest stones, with this hint we can come to the conclusion to use a max heap 

        # one important thing to remeber do, would be that we cannot use a max heap, we use a regular heap, but with the negative sign 



        heap = [] 

        



        for x in stones: 

            heapq.heappush(heap, -x)


        # okay now we have our heap, so we want to grab those values in the heap


        while len(heap) > 1:
            
            y = -heapq.heappop(heap)

            x = -heapq.heappop(heap)  # we put the negative in both so that they can rever to postivie values, keep in mind that all the values are postives 


            if x == y:

                continue 

            
            elif x < y: 

                new_value = y - x 

                heapq.heappush(heap,-new_value)


        if len(heap) == 0:

            return 0 

        elif len(heap) == 1:

            return -heap[0]

                


            