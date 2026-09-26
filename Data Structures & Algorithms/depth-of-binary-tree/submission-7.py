# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        # okay the way we do this is that we go all the way down to the tree and when we come back up we will count every time we come back from the recursion, becasue whenever we come back that means that we already explore what is beneath. 

        # we then compare the left and the right to see if any went further, and once we doo that we get the max between them and that will be our depth 


        if root == None: 

            return 0

        left = self.maxDepth(root.left)

        right = self.maxDepth(root.right)


        return max(left, right) + 1 


        # in the first example this will return 2 



        