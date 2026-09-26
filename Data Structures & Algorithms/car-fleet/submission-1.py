class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # we are given position, and speed, both of who are the same length, which is n
        # n = cars traveling the same destination 

        # position is the position of the car, for example if we have [1,2,3]
        # the position of the first car will be 1
        # the position of the third car will be 2 and so on and on 

        # speed is the speed of the car, if we have [1,2,3]
        # the speed of car 1 will be 1 
        # the speed of car 2 will be 2 and so on and on 

        # their destination will be set in target 

        # a car cannot pass another car, if a car catches up to a car, then they will both have the same speed 

        # a car fleet is cars or car driving at the same speed 

        # if a car catches up to another car or a group of cars, then it will be considered for that car to be part of the fllet 


        # return the group of cars or car that arrive to the destination 



        # example = Input: target = 10, position = [1,4], speed = [3,2] 

        # car1 = 1, speed 3  car 1 = 1, 4, 7, 10 
        # car2 = 4, speed 2  car 2 = 4 , 6, 8, 10 

        # as we can see in this example both of the cars meet at end. so the output is 1 



        # okay this is what im thinking 

        # a really good tip for this quesiton is to know the triangle of time, speed, and distance:

                        # ditance 
                    #speed      #time 

        # so with this we can calculate their times, and if their times are smaller and they start before another car and their time is bigger, then by defaul that would make them a car fleet 


        # for example  target = 10, position = [1,4], speed = [3,2]

        # here we have:

        # position 1 time: 10 - 1 = 9 / 3 = 3 
        # position 2 timeL 10 - 4 = 6 / 2 = 3 

        # they both have the same time so the output will be 1 


        # so this question is actually really hard, and if im being honest, i dont think i would had been able to figure it out by myself

        # but what we want to do is first a thing that i didnt know we could do. but 

        # we can save up the pairs of our numbers into a zip 



        cars = list(zip(position,speed))  # this will make it that the position is saved with each speed:

            # cars = [[1,3], [4,2]] 


            # now what we want to do is we want our values to be from the biggest position to the smalles position
            # we will do it like that so that we have the numbers closest to the target, this way we can see if the number before that one is bigger or smaller time than the one before it 

        cars.sort(reverse = True) # we want from smalles to biggest 

            # target = 10, position = [4,1,0,7], speed = [2,2,1,1], use this examples to get a better idea 
        
        # so now we have cars = [[7,1], [4,2], [1,1] , [0,1]] 

        # so now we have this 
        stack = []

        for position, speed in cars: 

            time = (target - position) / speed # this will give us their time 

            if not stack or time > stack[-1]: # if the time is bigger than the previous one then append that time  

                stack.append(time) 

            # so what will happen here, is that we will get stack = [3] 

            # then we will comapre the time of the next one, with the previous time, and if the time is bigger, then we can go ahead and included it on the stack
            # becasue the number that there will be in the stack, will be equivalent to the cars that made it 

            # stack = [3]

        return len(stack)
         
