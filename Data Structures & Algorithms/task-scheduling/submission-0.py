import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # for this question we have to keep in mind that we are trying to get the letter that have the biggest frequency
        # because if we get rid of the one that has the biggest frequency first, then that decrements the chances of us having to wait for it to iddle, because remeber that
        # "identicals task must be separated by at least n" 

        # we want it to look like this: 

        # frequency = {X: 2, Y:2}

        # Now we want to use a max_heap, so that we can have the one that has the biggest frequencies on our heap, that way we always know which has the most frequecnies

        # ok now comes the hardest part of the code

        # we want to use time. 

        # we will use a queue, and time so that way we can incremenet the time + 1, as we get a new value, 
        # but more importantly, this way we can keep track of how long we need to wait for the next value. 

        # so in the queue, we will have queue = [frequency of letter, remainding time] #

        # and the remainding time will be time + n, becsae time is the current time we are in, and n is the amount we hav to wait. 

        # lets me give you an example so that we can understand it more
         
        
        # ["X","X","Y","Y"]  n = 2

        # we use x, and  n = 2. that means that i have to wait at least 2 time to use it again

        # now look at the time

        # time = 1, when we pick the X

        # time = time will be 3 seconds after we can use A again.. why?

        # time: 1(x) ,  time: 2(can use what i want, lets say Y), time: 3(can use what I want, let say Y): time: 4 (finally I can use X again)

        # seems confusing at first but we have to keep in mind that i need to have 2 separate of space in between them 

    


        # now when the time we calculate is the same as the time we have now. that means that we can take the first queue that we had
        # the first queue, will always be the first element we got.. which would be the biggest at the time, and we can finally pop one from that queue 


        # lets go by parts 

        count = Counter(tasks) # this would set our frequency 

        # count = {X: 2, Y:2}

        # create the max_heap 
        max_heap = []
        
        for frequency in count.values(): # when we do count.values, that means that we will only see the values of the frequencies

            heapq.heappush(max_heap, -frequency) 

        # we have created our max_heap using the frquency values. ill do a drawing next to this, so that i can understand better 

        # now we need to create the time variable.. and for that we need a queu

        queue = deque()

        time = 0

        while max_heap or queue: # if any of the queue or the max_heap, still have something, then we will kep on going


            time = time + 1

            if max_heap: # if there is something in the max_heap, then we need to use it, and put the reamaindings in the queue, also with the time we will be able to use it again 

                # we need to get rid of a the one with the biggest frequency 
                current_max_heap = heapq.heappop(max_heap) + 1 # so the max_heap is -2 so we need that to be 1. once is 1. it means we got rid of it 
                # and the max_heap, should fix it self 

                if current_max_heap != 0: # if the current didnt make it to be 0, it means that there is still more to that max_heap, that we need to come get later on 

                    queue.append((current_max_heap, time + n)) # so we need to still eventually return that current. and we need to save the time that we are on, which is 1, and the n that we are
                    # becasue we will only be able to use this element again after 1 + 2 = 3. happened, so in time 4 we can use it again

                    # x -> y -> iddle -> now could use it again. 4 times later 

            if queue and time == queue[0][1]: # if the time == the time for another queue to be ready, then that means that we can pop the queue, and use that one 
                current_queue = queue.popleft()[0] # now we have the queue heap, that is ready to be use 
                heapq.heappush(max_heap, current_queue)

        return time 



# when i come back, run this code, and see what it does is pretty crazy 

# so the first thing we are going to get the frequency, which will be 

#  count = {X: 2, Y:2}, then after that we will get the max_heap of each using only the frequency par t

# so we will have a max_heap of 2 -> 2 . and remeber that the numbers are negative so keep that in mind

# then if we have something either in the queue, or the max_heap, we are going to go thorugh the while loop and get the time

# wverytime we start a new process we will get new time, then we will see the max frequency of the max_heap, and we will pop that out and put it on the queuwe
# then we will see if the time matches the time that they have to wait, and if it does then we will pop the queue and put that on the heap, so that it can be process again, 
# and then we keep on doing that as a cycle 
