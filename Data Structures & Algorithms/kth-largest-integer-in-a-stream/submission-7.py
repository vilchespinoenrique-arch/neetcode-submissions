import heapq
class KthLargest:

# what we want to do in this question is we want to use a min-heap, to get the biggest elements, now you might be asking why do we want to do that

# lets set an example of why we would do this,

# lets say we have [1, 3, 4, 5, 8] and we want the k = 3 biggest number that measnt the third biggest number 

# by knowing this we put in the min heap the top 3 biggest elements, what will happen is that we will get the third biggest element in the root of our min heap 

# lets look an exaple 

# lets say k = 3 

# first value we will have 1 

# heap = [1] # right now we need to fit 3 numbers so it doesnt matter what number it is 
# heap = [1, 3] 
# heap = [1, 3, 4] 

# now we will only add a number if the next number is bigger than any previous numbeer 

# is 5? bigger, then we remove the current smalles value, which was 1 

# heap [5, 3, 4] 

# now is 8 bigger than 3? 

# it is, so we remove it 
# and we now have

# [5, 4, 8] and in he heap visual 4 would be in the root, becasue is the smalles one, now we would just print the 4 right becasue is at the top and that would be the kth biggest value 
    def __init__(self, k: int, nums: List[int]):
        
        # just so we know using the import heapq, we are able to use the heapq.heappush(heap, number)
        # and this will create an automatic heap, where the first number is always the smallest 
        self.heap = []
        # lets create our heap
        self.k = k

        for num in nums: 
            heapq.heappush(self.heap, num) # this will create our heap 

            # there is a small thing that i forgot, we created our heap, but we have to maintain in the range of k so.. 

        while len(self.heap) > self.k:
            heapq.heappop(self.heap) # if we are exeding that number, then go aheadn and erase it so that we can have normal values 
        

    def add(self, val: int) -> int:

        # now how i said before, what we want to create here is a heap whre only the top k elements are here, and we return the smallest of those 

        if len(self.heap) < self.k: # of the k is bigger than the current heap, that means that we can put a value on there 
            heapq.heappush(self.heap, val) # here we will include the firt value 

        else: # else.. meaning if we already have the 3 values in there 
            if val > self.heap[0]: # if the value is bigger than the current value, the smalles value, has changed to that one 
                heapq.heapreplace(self.heap, val) # this will take the smalles current value, and it will put the current value as the smallest, and then it would fix the heap 
           
                # ignore that value 
        
        return self.heap[0] # always return the top value, becasue that one will be the curent kth largest element 

        # lets try this 

        # we have k = 3, [1,2,3,3] 

        # the first 3 elements will be created. so we will have 

        #                   1 
        #                 /   \ 
        #                2       3   

        # now when that 3 comes aroud, we will have to comapre 3 > 1? if it is, then it menas that the current 3 biggest values, have changed, and we have to replace that 1, with the 3 


        #                     3 
        #                 /   \ 
        #                2       3  
        # but as we do that the heapreplace, also fixes the heap for us. so it will look like this, really 

        #                   2 
        #                 /   \ 
        #                3       3  

        # the smallest element being that 2. so right now the 3th biggest element is 2. 
