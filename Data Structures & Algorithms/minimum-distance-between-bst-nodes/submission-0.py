# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:


        # for this question is wise to have a prev, and to have a current one, so that we can compare each possible node, 


        # so we will compare 1 and 4, 4 and 7, 4 and 10 and so on and on... you get the point? 

        # that way we will do all of them, 


        # we will go throught the iterations so that we can see the difference 


        prev = None 

        best = float('inf') # best is infinite right now 


        def check(node): 


            nonlocal prev, best # meaning that they will not get restarted everytime 


            if node == None: 

                return  

            check(node.left) # lets go all the way to the left 


            if prev != None:   

                best = min(best, abs(node.val - prev))


            prev = node.val 

            check(node.right)

        
        check(root) 

        return best 






 

        