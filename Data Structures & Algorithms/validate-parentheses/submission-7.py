class Solution:
    def isValid(self, s: str) -> bool:

        # we need to understand that we can use a stack for this, and the reason for this is because anythin we get will be hold till we can match it with something that will come after.
        # so we will compare the last element we get with the current element we are getting 

        # think of the inputs 

        # input: s = "[]"
        
        # Input: s = "[(])"
        
        # Input: s = "[(])"

        # input: s = "]"

        # the idea behind what we want to do is, for every open bracket we get, then we need a closing bracket, so we will be comparing that. 

        dictionary = {')': '(',   ']':'[',   '}':'{' }

        stack = [] # we are going to use a stack to hold the values that come in

        for char in s: 

            # i have run into the problem, of what should i do to only hold open brackets here, and not close brackets
            # i came with the idea to use a dictionary for this
            
            if char in dictionary.values():
                stack.append(char)
            # this line of code makes it so that we only get open brackets 

            # now we need to put ourselves in 3 situations 

            # we could either
            # 1) get a weird number
            # 2) get a close bracket that matches our open bracker

            # this are the 2 possibilites of thing that can happen

            # here we got char to be a closed bracket 

            elif char in dictionary: 

                # now they are 2 situations for this closed bracket, it could either be after an open bracket, or the first element being an open bracket 

            
               

                # if our closed bracket is a closed bracket after the open one, then we will pop the last element becasue we had a match

                # now what if the value was a first closed bracket, that should return false right away 
                if not stack or stack[-1] != dictionary[char]:
                    return False

                # lets say is after an open bracket 
                elif stack[-1] == dictionary[char]:
                    stack.pop() 

            
                

            else:
                continue 

        if len(stack) == 0:
            return True
        
        else: 
            return False


        #okay the code wasnt that bad, we were able to pass 9/32 cases. lets see what we missed

        # s = "]"
            