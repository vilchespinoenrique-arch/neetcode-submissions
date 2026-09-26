class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        # this quesiton can be solved if we usea a hashmap. now why would we use a hashmap? 

        # hashmaps are really useful whenever we want to keep a count of something. they are mostly use for dicionaries or matching things, and is perfect becasue the speed of it is 0(1) making it one of the fastest algorithm that there are. 



        # so my idea here is to use 2 hashmaps for each letter here and then compare them. there is a better way of doing this, with just one hashmap, but is easier for me to just use 2 hashamps, and then compare if they are equal 


# saddly i almost always forget how to set it up. but this is how you create the hashap table so that it goes through your array and takes counts each one

# for char in s:
  #          has[char] = has.get(char, 0) + 1


    # let me run you through this. 


    # so let say that we have a hashmap named has = {}

    # has[char], here the hashmap has, is being looked by char, which is whatever lets say is r. so in the hashmap it will look for that key r, and return the value, the value is what is attached to that letter. and then we have has.get(char,0), this is saying go get me the value of that char, and if is nothing returned it as 0 and then add 1

    # so for example for has[r] = 1. so if r where to have 0 it will now be 1, and that r would be linked to that r as the key and it would remain like this: 


#    has = { r : 1} 

# and then the same would happen with the rest 


        if len(s) != len(t): 

            return False 

# if they dont have the same len, you can go ahead an return false right away 


            
        hashmap1 = {} # the first hashmap has been created 


        for char1 in s: # we are going through the letters of s  

            hashmap1[char1] = hashmap1.get(char1,0) + 1 

# this would return us a already made hashmap 


        hashmap2 = {}

        for char2 in t: 

            hashmap2[char2] = hashmap2.get(char2, 0) + 1

# this would return us an already made hashmap for t 


            
        if hashmap2 == hashmap1: 

            return True 

            
        else:
            return False 


        