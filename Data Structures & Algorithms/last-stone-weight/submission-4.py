class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        


        heap = [] 


        # step 1 - create the heap 


        for x in stones: 

            heapq.heappush(heap, -x) 



        while len(heap) > 1: 


            y = -heapq.heappop(heap)

            x = -heapq.heappop(heap)


            if x == y:

                continue 

            elif y > x: 

                new_value = y - x 

                heapq.heappush(heap, -new_value)


        
        return -heap[0] if heap else 0 
