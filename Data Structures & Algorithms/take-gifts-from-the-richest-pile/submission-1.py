import heapq

from math import isqrt

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        

        # step 1 - make the heap 


        heap = [] 

        


        for x in gifts: 

            heapq.heappush(heap, -x) 

        # keep all the results in a heap



        
        for _ in range(k): # all the results are now in a heap, however we are not going to use all of them, only till we finish k, with the loop 

            biggest = -heapq.heappop(heap) # this will be the biggest one, in this example that would be the 100 

            biggest_square = isqrt(biggest)

            heapq.heappush(heap, -biggest_square)


        
        return -sum(heap)



    
