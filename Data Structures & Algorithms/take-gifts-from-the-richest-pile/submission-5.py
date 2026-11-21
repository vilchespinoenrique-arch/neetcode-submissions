import heapq
from math import isqrt

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        


        heap = []

        for x in gifts: 

            heapq.heappush(heap, -x)



        
        for _ in range(k): 


            biggest = -heapq.heappop(heap)

            bigges_square = -isqrt(biggest)


            heapq.heappush(heap, bigges_square)



        return -sum(heap)

