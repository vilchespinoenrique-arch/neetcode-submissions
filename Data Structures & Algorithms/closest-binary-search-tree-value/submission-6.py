# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        

        def check(node, closest): 


            if node == None:

                return closest 


            if abs(node.val - target) < abs(closest - target): 

                closest = node.val 


            if node.val > target: 

                return check(node.left, closest)


            else:

                return check(node.right, closest)
        
        return check(root, root.val)

            # lets run through an iteration


            # we have (root, 4) 


            # 4 - 3.714 = 0.286 , closest right now is 4, so this is the nwe closest

            # closest = 0.286 


            # now becasue 4 > target we have to go look on the left for something 


            # and then we start looking both sides 

