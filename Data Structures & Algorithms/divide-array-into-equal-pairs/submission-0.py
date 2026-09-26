class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        

        hashamp = {} 


        for num in nums: 
            
            hashamp[num] = hashamp.get(num, 0) + 1



        for value in hashamp.values():

            if value % 2 != 0: 

                return False 



        return True 
