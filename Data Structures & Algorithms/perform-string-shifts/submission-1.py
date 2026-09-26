from collections import deque

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        

        # this question is divided in parts 


        # 1) find the total shifts.. here is the thing, if you go to the left for 10 meters and then you go to the right for another 5 meters

        # that is the same as going to the left for 5 meters. so instead of us having to do all that, what is better is that we go to the left 5 meters inmediately 


        # for this common sense reason we can understand that we need a total amount of rotations, so that we dont go crazy going back and forth 


        # 2) after finding the total shifts, we need to move them 

        # for me the easies way to shift strings, is to do it by using a deque. there is a function in that library that handles shifts for you, which i found very useful 

        #   the steps for that is that we would have to transform our string into a list, and then glued back together into a string

        # trasnform from string to list = string = list(string)


        # trasnform from list to string = list = "".join(string)
    


        # there are special casses that we need to consider, for example what to do when the shift is bigger than the numbers, in that case we would use 

        # % becasue if we have 5 numbers and we are being ask to shift it 6, that is the same as 1, and we dont want to go crazy over that 


        total_shift = 0

        for direction, amount in shift: 

            if direction == 0: # it means we are going left, so we have to subtract 

                total_shift = total_shift - amount 

            else: 
                total_shift = total_shift + amount 


        
        # now we have our total shift we can use a deque 

        new_list = list(s)



        shifting = deque(new_list) # put the new list in the queue 


        shifting.rotate(total_shift)


        return "".join(shifting)