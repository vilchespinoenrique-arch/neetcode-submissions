class Solution:
    def findLucky(self, arr: List[int]) -> int:
        

        # step 1, get the numbers and their frequency 


        # step 2, only if your key is the same as you value, you can continue 

        # step 3, pick the biggest one in between that if statement 



        hashmap = {} 

        result = []



        for ar in arr: 

            hashmap[ar] = hashmap.get(ar, 0) + 1 


            # this is going to give me this: 


            # hashmap = {1 : 1, 2: 2, 3:3}


        for ar in arr: 
            
            if ar == hashmap[ar]: 
                
                result.append(ar) 



        if result:

            return max(result) 

        else: 

            return -1
                