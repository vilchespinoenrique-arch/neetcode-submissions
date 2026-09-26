class Solution:
    def isValid(self, s: str) -> bool:
        

        # firtst of all we need to know what a stack is becasue stack is perfect for this example 


        # stack is just like a panckake so it get there last and leave first. so as soon as something new arrived that same thing will be the first thing to leave


        # so lets say we have 


        # [1, 2, 3, 4] -> if they start coming one by one from left to right. in that case the last to arrive will be the first to leave 


        # this can be apply to this question 



        # so there a really importatn thing to this quesiton and that is that if we see that there is a open bracket. that last open bracket that we received has to be a close bracked of that type or it can be an opne bracket those are the only 2 options. 



        # my idea for this is to first apply a dicctionary of the types that we could get. 


        # i also want to set the open bracket as the key. becasue if we have an open braket key value that matches the close bracket it would mean that they are from the same type and then i would eliminate them right there. 




        # lets start with the hashmap then 



        dic = { ')' : '(', ']' : '[', '}': '{' }




        # lets use s first to find the easiest solution from the first example so that we can see an easy example 


        stack = []

        for char in s: 

            if char in dic or char in dic.values(): 

                if not stack or char in dic.values(): 

                    stack.append(char)

                elif stack and stack[-1] == dic[char]:
                    
                    stack.pop()

                else: 

                    return False 
                
            


        if not stack: 

            return True  

        
        else: 

            return False 


