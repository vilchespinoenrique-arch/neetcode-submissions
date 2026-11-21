import heapq
from math import isqrt


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        

        # first we create a heap, with everything 

        heap = []



        for x in gifts:

            heapq.heappush(heap, -x)



        # now that we have the heap with everything, we can go ahead and go throught it in k time 


        for _ in range(k): 


            biggest = -heapq.heappop(heap) 


            biggest_square = isqrt(biggest)


            heapq.heappush(heap, -biggest_square)



        return -sum(heap)