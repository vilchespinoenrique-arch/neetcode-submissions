class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        # want to create a hashmap first so that we know which chars are only seen once 


        hashmap = {}



        for char in arr: 

            hashmap[char] = hashmap.get(char,0) + 1 


            # this will create a key for each char, and an a values of the numbers of times we see it, so it will look like this: 


        # ["d","b","c","b","c","a"]

        # for this example, it would look like this: 


        # hashmap {d: 1, b: 2, c: 2, a : 1}


        count = 0 
        
        for char in arr: 

            if hashmap[char] == 1: 

                count += 1
                
            if count == k: 

                return char

        return ""





            

