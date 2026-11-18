import heapq 

class KthLargest:

# the way we will solve this problem is that we will move use a min heap. 

# a mean heap, means that every number that you get will set the smalles number in the top of the tree 

# this works perfect for us, becasue if we are trying to get the third, second or fourth biggest numebr we can use it 


# becasue in the min-heap we will always have the smaller value in the top, and the bigger value will go down the tree

# this means that we will have the top 3, top 2 biggest value, where the smalles of them will be in the top, which is exactly what we need


# things to consider are: 

# this is how you create your heap 

# heap.heappus(heap where will be stored, what will be stored)

# for num in nums: 
          #  heapq.heappush(self.heap, num) # this will create our heap 



        # this right here is setting so that when we exceed the heap, we the smalles number remove, and the smalles number will always be hea[0], for what i explained before
         # while len(self.heap) > self.k:
            # heapq.heappop(self.heap) 



    def __init__(self, k: int, nums: List[int]):


       self.k = k 


       self.heap = []

       
       # now lets go ahead and create the heap 

       for x in nums: 

            heapq.heappush(self.heap, x) 

            
            while len(self.heap) > k: 

                heapq.heappop(self.heap)
        

        # now we have our heap create 
        

    def add(self, val: int) -> int:


        if len(self.heap) < self.k: 

            heapq.heappush(self.heap, val)


        else: 

            if val > self.heap[0]:


                heapq.heapreplace(self.heap, val)

                

        

        
        return self.heap[0]
        
