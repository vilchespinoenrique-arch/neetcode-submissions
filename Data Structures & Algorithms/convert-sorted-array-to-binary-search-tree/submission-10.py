class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        pass
        
        # to convert an array to binary search tree, the first thing we want to do is 
        # get the middle, then we will have a low and high, that will be going thought the array, and adding them as the binary searc h


        def check(low, high): 

            
            if low > high:
                return None 


            mid = (low + high) // 2 


            root = TreeNode(nums[mid])


            root.left = check(low, mid - 1)


            root.right = check(mid + 1, high)

            
            return root 

        
        return check(0, len(nums) - 1)