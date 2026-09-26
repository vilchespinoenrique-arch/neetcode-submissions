class MinStack:

    def __init__(self):
        
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:

        if not self.min_stack or val <= self.min_stack[-1]:  # this will make it so that we keep the smallest elements always
            self.min_stack.append(val)
        # we want to push, so we want to add the val into our stack
        # but on the other stack, we also want to have a min_stack that has the smallest value at 

        self.stack.append(val)


        

    def pop(self) -> None:
        

        # this is the challenging part of this code. we do not want to remove the stack and min stack all the time. we want only to remove the smalles_Stack when it has been removed in the stack
        # in order to do this, we can remove the min_stack, whenever we have the stack being the same as the min_stack. it fits perfectyl
        # becasue when we put our values on min_Stack, is going to be the same placement that the values in the min_stack.
        # lets better look an example instead of me telling you 

        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        # stack = [1,2,3,4]
        # min_stack = [1] 
        self.stack.pop()
        
        # now when we remove the stack we can do that all the time, but with the min_stack we will remove only when the stack and the min match 

        # pop(): 

        # stack = [1,2,3]
        # min_stack = [1] 


        # pop():
        # stack = [1,2]
        # min_stack = [1] 

        # pop():
        #stack = [1]
        # min_stack = [1] 

        # pop():

        #stack = []
        # min_stack = []

        # we finally erase the min_Stack because it was the minimum between the two 

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]        
