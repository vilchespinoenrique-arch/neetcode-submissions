class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # for this question the first thing that we need to know is that reverse polish notation works really well if you have a stack
        # the reason i say this is becasue lets see and example and you will see how the stack is being used 

        # rever polish notation: 

        # we have [1, 2, +, 3, *, 4, -]

        # the idea behind using a stack. 

        # is that we will be using the numbers that we are getting: 

        # we will get 1, put it on the stack 

        # stack = [1]

        # then we will get 2, put it on the stack

        # stack = [1,2]

        # now we will get + 

        # if we see an arithetic 

        # we will take the previous values, 1, 2 and we will add them togethere

        # we see + 

        # we add 1 + 2 = 3, we then remove those 2 numbers and we only stay with the 3 

        # stack = [3]

        # and we keep on going 

        # stack = [3, 3 ] and so on and on 


        # something that i missed that made me struggle throught this question where 2 things. 
        # the first that i did not do this, which kind of simplifies my problems 

        # a = stack.pop() 

        # i forgot that you can pop an element but save it in another varible, which would of been really helpful to do

        # the second thing being that if we have for exmaple [3, 5, 7 + ] # this here means that we only add the 7 and the 5
        # we do not add the 3 asswell, this is an error and we would just leave that 3 behind, it wouldnt change anything really 


         # tokens = ["1","2","+","3","*","4","-"]

        stack = []

        for t in tokens: 
            
            if t in {"+", "-", "*", "/"}: 
                a = stack.pop()
                b = stack.pop() 
                # as soon as we see any of this elements it means we are good to pop 

                if t == "+":
                    stack.append(b + a)

                elif t == "-":
                    stack.append(b - a)

                elif t == "*":
                    stack.append(b * a)

                else:
                    stack.append(int(b / a)) # this way if the asnwe is 2. 5, it will make to be 2 

                
            else:
                stack.append(int(t)) # because they set them as string 

        return stack[-1]

        
        
        