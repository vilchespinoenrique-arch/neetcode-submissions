class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:


    # step = 1  get the count of each character 




        hashmap = {} 

        


        for char in text:

            hashmap[char] = hashmap.get(char, 0) + 1 



            # this will give us a list of and count of each element 


            # hashamp = { n: 2, l : 2}  and so on and one 

    
    # step 2: we want to get the min of our counts. why would we want to do this? 

    # if we look for the minimum, we would know how many ballons we can have

    # so for example if we have n = 1 a = 2, l = 2, o = 2, b = 1, eventhough we have 2 a, which could help us make 2 ballons we want to have to the minimum of what we have,

    # which is b = 1, and that could only give us one ballon. we also have to keep in mind that we want to erase divide by 2 the l and the o, becasue for every 2 of those we have 1 


        
        b = hashmap.get('b',0)
        
        a = hashmap.get('a', 0) 

        l = hashmap.get('l', 0) 

        o = hashmap.get('o', 0)

        n = hashmap.get('n', 0)



        return min(b, a, (l//2), (o//2), n) 








        