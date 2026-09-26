from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # for this question we can use something called counter 

        count = Counter(nums) # now inside count it will appear like this: 

        # count = {5:4, 1: 3}
        
        # now if we want to get the max, the one that has the most elements, the only thing we need to do is: 

        return max(count, key= count.get)