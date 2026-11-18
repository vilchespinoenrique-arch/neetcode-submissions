class KthLargest:

    # something to mention and understand is what does 

    # heapq.heapreaplce(self.heap, val) , first item will take the self.heap, which is the top of the heap, and val 

    def __init__(self, k: int, nums: List[int]):

        self.k = k 

        self.heap = []


        for x in nums: 

            heapq.heappush(self.heap, x)

            while len(self.heap) > k: 

                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:


        if len(self.heap) < self.k: 

            heapq.heappush(self.heap, val)


        
        else: # where the len heap is full 


            if val > self.heap[0]: 

                heapq.heapreplace(self.heap, val)

        

        return self.heap[0]
        
