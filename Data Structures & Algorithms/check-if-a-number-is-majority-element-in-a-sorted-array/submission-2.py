from collections import Counter 


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:



        count =  Counter(nums)


        # now we have the count of nums

        majority = len(nums) // 2 


        for key, value in count.items(): 

            if key == target: 

                if value > majority: 

                    return True 

        
        return False 
        