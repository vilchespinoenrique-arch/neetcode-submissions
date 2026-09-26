class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # what we are being asked for this question is to get set a result list, where we can put the days it took to find a warmer termature 

        # what im thinking for this quesiton is to have the answer saved in stack. but apart from that. i think this question is pretty foward

        # we just want to go through each one using an array

        # now the main problem comes on how we are going to be moving through the array, my main thoguhs are either with 2 for loops,
        # the problem with this is that if i do that it will be 0(n^2), which we dont want 

        # my second idea is to two pointer that could be better. or i think the best option would be a for loop with a while loop, that way we would inmediatelly stop once the number is bigger, and we would set the result on the stack 


        # the best wat to solve this problem is with using a stack. now it can get complicate so lock in lol
        # we are going to use a stack and that stack is going to keep track of the indexes, so that way we can know in which index we are

        # if we know in which index, we are we can easily subtrac from that index, and the index that we are currently on, and that would give us a distacne on how far we travel 

        # the other thing is that we need to keep in mind, is while we dont know the warthmest dame for some indexes, that doesnt mean that we cant compare the next one in line while we compare the one before that

        # i know it might sound confusing, however, i will explained with an example 

        # for that very reason we can keep a list with result, where result can be stored in different indexes, depending on where we are 



        result = [0] * len(temperatures)
         
        stack = []

        for i, temp in enumerate(temperatures):
            
            while stack and temp > temperatures[stack[-1]]: # if the number that we are on is bigger than the previous one, we did it we found a match
            # so we can calculate the distance in between those 2 and save that difference 
                prev = stack.pop() 
                result[prev] = i - prev # the result will be the difference between that last element and the element we are currently in 

            


            stack.append(i) # in here we will every index that we go through

        return result 


        # lets go through an example so that we can see everything on action 

        # temperatures = [30,38,30,36,35,40,28]

            # 1) stack = [0]

            # 2) is 38 > 30? yes.. then we can put our previous stack into the result, and put it for that one

            # result[0] = 1 

            # # since we already used that numbr, and we dont want to re-use it. we did erase it. 

            # stack = [1], only 1 becasue remeber that we did erased the 0 


            # 3) is 30 bigger than 38? no. okay here is the imporant part that i need to understand. when we realized that 30 isnt bigger than 38

            # instead of being o darnm, we cant keep going untill we find that other element. instead of doing that, we will save that index, and compare it with other while we compare the other number as well
            # so we are doing 2 comparisons at the same time 

            # stack = [1,2] # remeber we still save that stack 

            # 4) is 36 > 30? yes it is, this means that the last index we just visited has found his warmthest day! 

                # result[2] = the difference of the element we checked and where we were.. so 3 -2 = 1 
                # result[2] = 1 

                # the result table now is looking like this 
                # resul = [1,empty, 1], which so far is accurate... lets keep going, we are still inside the while loop, the reason why this is a while 
                # loop is because it could happen that 36 is bigger than 30 . but now we need to check if that 36 is bigger than 40
                # which in this case it isnt. so we stop 

                # stack = [1, 3] # notice how the stack has indexes that we havent calculated yet, becasue we havent found there warthmest day yet 



            # 5) is 35 > 36? it isnt, so we put it on the stack and we keep going 

                #stack = [1, 3, 4]
            
            # 6) is 40 > 35? yes so it means that we have found a match for index 4 

            # result[4] = difference of the index and where we are now = 1 

            # result = [1, empty 1, empty, 1] 

            # this is a while loop so we can keep checking the other indexes. is 40 > 36? 

            # it is, which means that we also found the index of that one!! yey

            # stack = [1,3]

            # result[3] = 5 - 3 = 2 # their distance is of 2, thats great!! 

            # lets keep in going. 

            # is 40 > 38? it is! finally we have found it 

            # result[1] = 5 - 1 = 4 

            # result = [1, 4, 1, 2, 1]

            # and then you keep going but you get the idea 



            # the key idea to get from this problem is that we where able to use a stack, and their index to compute and find which one was b
            # the key thinking is that when one number didnt have a match, we wouldnt trip and keep going until we found that other number.. we would save that number in our stack and
            # we would keep going with the other numbers and checking with them on the stack, and when we found it for them, we would remove them... and guess what the other number 
            # will still be there... so it wouldnt bother us at all. this made so that we only need to go throught the array once
            # we save those numbers inside our stack and when we found a smaller number we wouldnt care and we would save the index of that number and keep going, and find the bigger number of the next... and so on and on, and once we found it, we can erase their index in our stack
            # and we can check the last one we didnt do.... a stack!!! 

