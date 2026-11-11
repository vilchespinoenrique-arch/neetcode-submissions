class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        pass


        # for this question we want to set a mid, and then do the same idea that we would do with a binary search 


        def check(low, high): 
            
            if low > high: 
                
                return None 
            
            m = (low + high) // 2 

        

            root = TreeNode(nums[m])


            root.left = check(low, m - 1)


            root.right = check(m + 1, high)


            return root 

        
        return check(0, len(nums)- 1)