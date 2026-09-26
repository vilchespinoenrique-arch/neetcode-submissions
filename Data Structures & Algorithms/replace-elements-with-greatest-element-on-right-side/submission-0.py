class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # just for better clearance when working with range

        # range = (start, stop, step) 

        # so if we have(10, 0, -1) 

        # it means we start at 10, we stop at 0, and we move backwards 

        # what im about to code might seem a litle confusing 

        # because it will seem like we are skipping one element, however as i do it, it will make more and more sense 


        # firs thing, when we look at this, we should look at it from the left perspective

        # because i first was like why dont we go to from left to right, and we find the biggest one yet, and then we put in a ponter, 

        # and we use anothe pointer to move throught the array 

        # the problem with this is that it would become brute force, becasue even thought we have 2 pointers we are moving to the rights constinuosly, and coming back and then moving back again.

        # making it a big problem 



        # now instead of doing that we can look at this problem from the right and have a current max value starting from -1 


        # that is actually really clever to do 

        # we will saev the current value that we have, we will then replace the index, that we have with the biggest value so far, 

        # that it will be a -1, currently, and then we will see if the current value that we have is bigger thatn the last value 

        # if it is bigger then we are going to change that biggest values, and then that biggest value will be the right asnwer 

        # i want to show how this could be confusing... but let me code it first 



        max_value = -1 


        for i in range(len(arr) - 1, -1, -1): # this is saying we will start at the end of the array, and then we will move backwatds until we hit - 1

            current_value = arr[i] 

            # first thigs first, save that current value 

            arr[i] = max_value  # the max_value will be the one replacing the ucrrent index 


            if max_value < current_value: 

                max_value = current_value 

                # if the current_value is bigger than the max_value, then you can go ahead and replace that max_Value for the new value 


            # at first this will look like this: 

            # [2,4,5,3,1,-1]

            # [2,4,5,3,1,2]

            # then since 2 is bigger than -1, it will become the new max_value 

            # so now we will replace in the next one 

            # [2, 4, 5, 3, 2] 

            # now is 2 > 1? it is, so we wil replace and change it in the next one 

            # [2,4,5,2,2,-1] # 2 so far was bigger than -1, that is will we replaced it and 1... that is why he took both of their spots 


            # is 2> 3? it is not, so 3 now becomes the biggest value 

            # [2,4,3,2,2,-1]

            # is 5 > 3? it is so, we replace the max_value 

            # [2, 5, 3, 2, 2, -1]


            # is 5 > 4.. it is 

            # [5, 5, 3, 2, 2, -1]

            # and now we finish here, because there is no more 

        return arr 

