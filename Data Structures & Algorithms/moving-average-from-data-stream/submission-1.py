from collections import deque 

class MovingAverage:

    def __init__(self, size: int):
        
        self.size = size

        self.list = [None] * size

        self.list = deque()

        self.total_list = 0

        

    def next(self, val: int) -> float:



            self.list.append(val) 

            if len(self.list) == self.size + 1: 
                
                number_gone = self.list.popleft()

                self.total_list = self.total_list - number_gone    

                


            self.total_list = self.total_list + self.list[-1]



            return self.total_list / len(self.list)




        

        #  a few thing to think about here, one of them being, we wont need to use a for loop in this problem becasue we are calling a new function everytime, so we also have to think of the variable that will be changing within time... everytime we call a new function something that would save the previuos ones, and that is a list 


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
