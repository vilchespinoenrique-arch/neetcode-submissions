"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:


        # so children are different, they can be 4 or they can be 10. for this reason we want to get them in a for loop, and go throught all of themm 

        result = []


        def check(node): 


            if node == None: 
                
                return 


            for children in node.children: 

                check(children) # this way we will go 1 by one 


            result.append(node.val)


        check(root)

        return result 

             


        