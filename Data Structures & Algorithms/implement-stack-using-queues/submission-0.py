# this question might me slightly confusing at first, but what we want to do is create two 

# queues, when we have those 2 queques,

# one of the queues will be use to hold the value momentarily, and then we will add the rest of the values to the other queue, that way we will have our newst value at the fron of the line

# is a cut the line kind of effect, it will look pretty cool 

from collections import deque



class MyStack:

    def __init__(self):


        self.queue1 = deque()

        self.queue2 = deque()

        # here we just create 2 queues 



    def push(self, x: int) -> None:

        # this is the most important part, we are going to first hold the new values in the queue1 

        if not self.queue2: 

            self.queue2.append(x) # if the queue is empty we are going to append something to it 

            return
        # queue1 will be the one responsible for holding the value momentarily 

        self.queue1.append(x) 

        # lets say this is queue = [1] 


        # then queue = [3,2] # and we have those values, we have to move the rest of this values to the queue 2 

        while self.queue2: # while the second queue has some values we have to 

            current = self.queue2.popleft()

            self.queue1.append(current) 

        # instead of doing this again.. we can just swap the names and that is ok. however i like it like this 


        while self.queue1: 

            current = self.queue1.popleft()
            
            self.queue2.append(current)


        # lets see if this will work. we have [3, 2]   in the second queue, and then we need want the new value to be at the front 

        # so first thing queue1. will have the [1], then it will have [1,3,2] and now if we want the one we just pop     

    def pop(self) -> int:

        pop_value = self.queue2.popleft() 

        return pop_value # you want this returned ? 

    def top(self) -> int:
        
        return self.queue2[0]

    def empty(self) -> bool:
        
        return not self.queue2 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()