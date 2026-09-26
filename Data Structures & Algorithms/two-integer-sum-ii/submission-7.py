from typing import List 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # what you want to do for this question is to get our array, which in this case is

        # [1, 2, 3, 4]

        # and what we want to do is set 2 pointers. 

        # left and right pointer, and becasue the number are in order we can do a binary search using 2 pointers 

        left = 0 
        right = len(numbers) - 1 

        # (1,2,3,4)

        while left < right: 

            value = numbers[left] + numbers[right]

            if  value == target:
                return [left + 1, right + 1]

            elif value > target: 
                right = right - 1 

            else: 
                left = left + 1 

            
        # lets test this solution: 

            # value = 5.  target = 3 

            # right = 2 

            # value = 1 + 3 = 4 

            # right = 1 

            # value = 3 . target = 3.. correct 



