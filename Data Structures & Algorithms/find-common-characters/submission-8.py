class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        

        # what we want to do here is we first want to count the amount that each letter has in a hashmap



        # so what we want to do for this question is to get the the first hashamap and compare it with the others to, and get the minimum to check for possible matches 



        hashmap = {} 


        for ch in words[0]: 

            hashmap[ch] = hashmap.get(ch, 0) + 1



        # now we have the first word looking like this 

        # [b: 1, e: 1, l : 2, a:1 ]



        # so now what we want to do, is we want to create a new hashamp word for word, so that we can compare it to this one, and find the minimum between each, becaue whatever the min is, is the amount of times we have to print that letter 


        for word in words:

            count = {} 

            # here count will be a new hashmap for each word

            for char in word: 


                count[char] = count.get(char, 0) + 1 


        # nowe we have the next word in a diccitionary, so it will look like this: 

        # {l : 2, a : 1, b : 1, e: 1}


        # now that we have we can compare them, in order to compare then and get a min for the words that are related to each other         

            for ch in hashmap: 

                hashmap[ch] = min(hashmap[ch], count.get(ch, 0) ) # we set it as 0, because in here we are going to see what value, we have from the value we are comparing, but if that value, doest exist then we want to set it to 0, becasue it measn that value cannot be added. 



            # then after the fact it will do the same with any word that is coming this way 


            # so now we will have something like this 


            # hashmap = {e : 1, l : 2}
        
        result = []


        for key, value in hashmap.items(): 


            for i in range(0, value):

                result.append(key)


        return result 























