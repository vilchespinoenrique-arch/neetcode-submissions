class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        # i didnt know this, or maybe i forgot, but you can put name of your hasmpa.items() 

        # and then n, r, and n will be you key, and r will be your dicctionary, so i thought that was cool 


        count = {} 

        # we are going to create a hashmap, to have a count of every element, and how many times we have seen those elements 

        for n in nums: 

            count[n] = count.get(n, 0) + 1 # this is saying if we go to n in the hashmap and we dont find the number.

            # then go ahead and add one 

            # at the end of this we will have

            # count = {5 : 1, 7: 1, 3: 1, 9: 2} 

            # and so on 

        max_current = -1 


        for key, value in count.items():

            if value == 1: 
                

                max_current = max(max_current, key )


        return max_current 