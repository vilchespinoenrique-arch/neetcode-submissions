class Solution:
    def mySqrt(self, x: int) -> int:
        

        # this question is really similar to the question that we solves before with the square root. the only different is that if we get a number that we want to rounded down, we would use the right for that. and i will show you how. enrique from the future!!! hope you got a job bro fr- also im 26 right now and im in top shape. got a 310 for deadlift and max everything but the deadlift and the sprint drag carry, but im really close, i have like 3 weeks left to train for it, and i think i will end up getting 330 on deadlift, i would be really happy with that really. so hopefully i get it. but my main worries are findin a job and a girlfriend lol. I wonder how it will be like after like 2 years that i look at this. i wonder where ill be at, phsycically and mentally. its crazy that my main worries right now are money, finishing rotc, getting my best aft, and finding a job, and getting married, feel pretty old really. but we will see what happens really!!!!! thats all but wheever you are in the future hopefully you are happy doing what you like. im writting this in the rotc unit, so thats good to know. i wonder who will read this. hopefully me! all love, you got this 

        left = 0 

        right = x

        while left <= right: 

            
            mid = (left + right) // 2 


            if mid * mid == x: 

                return mid 

            elif mid * mid > x:  # if the mid is bigger than the number then we are going to go lower 
                right = mid - 1 

            else: 

                left = mid + 1 

        
        return right 




