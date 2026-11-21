class Solution:
    def maxDepth(self, s: str) -> int:


        # there is a patter to this, if we are able to find the open parehtensis, then we can keep on going, and we find a close one we subtract. whatever top value we get, that will be the answer 


        result = 0

        count = 0 


        for char in s: 

            if char == "(":

                count += 1 

            elif char == ")":

                count -= 1 


            result = max(result, count)


        return result 
        