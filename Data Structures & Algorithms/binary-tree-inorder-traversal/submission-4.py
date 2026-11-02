# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # probably forgot but inorder is 

        # is left -> root -> right 

        result = []

        def inorder(node): 


            if node == None: 

                return 


            inorder(node.left)

            result.append(node.val)

            inorder(node.right)

        
        inorder(root)

        return result


        # lets go step by step and see what is happenign 

        # we start at node 1, then since that the root 