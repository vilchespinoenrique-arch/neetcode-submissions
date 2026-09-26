class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # for this question what they want us to do is to create the array and right after creating it, just create an exact duplicate of the same array that continues the list 

        ans = [] # attach everything into a list 
        
        n = len(nums)


        for i in range(0,n):

            ans.append(nums[i]) # we first attach the first nums in this loops

            # so ans would look like this: 

            # ans = [1,4,1,2]


        for number in nums: 

            ans.append(number)


        return ans
        
        # here this would be 

        # here the the ans would look into itself again and get repeated in the ans 

        # so now it should look like this: ans = [1, 4, 1, 2, 1, 4, 1, 2]
        