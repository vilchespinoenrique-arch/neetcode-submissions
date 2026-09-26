from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # firs thing we want is we want to have a queuque that will have all the values 
        if not node:
            return None


        queue = deque([node]) #now we have all the values of the node 


        clone = { node: Node(node.val)}  # here we are attaching the new node to a new node, that way we can have our deep copy 

        # this will look like this: 

        #  clone = { 1 : newnode(1)}, and then that 1.. is connected to the rest via the queue, so we will be able to use it 



        while queue: # as long as there are still numbers in the queue we will keep on going

            current = queue.popleft() 
            
            for neightbor in current.neighbors:  # if the current element we are using is not in neighbors, it means then that we need to conver the 

                if neightbor not in clone: # so if the current element that we have has not been cloned and also it has not in the neighbors, we can cloen it 

                    clone[neightbor] = Node(neightbor.val) # we need to attach the orginal value to the new value
                    queue.append(neightbor)
                    # it will look like this clone[2] : new(2)
                    
            
                clone[current].neighbors.append(clone[neightbor])


            # in here we are attaching the previous value, which was 1, into the new create value, that is saved in clone neighbor 

        return clone[node] 