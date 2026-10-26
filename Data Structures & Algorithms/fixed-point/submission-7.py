class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        pass


        left = 0 

        right = len(arr) - 1
        
        smaller = -1
    

        while left <= right: 


            mid = (left + right) // 2 



            if arr[mid] == mid: 

                
                smaller = mid
                
                right = mid - 1  
                
            
            elif arr[mid] < mid: 

                left = mid + 1 


            else: 

                right = mid - 1

        
        
        return smaller  