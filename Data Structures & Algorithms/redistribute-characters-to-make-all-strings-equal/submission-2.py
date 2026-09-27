class Solution:
    def makeEqual(self, words: List[str]) -> bool:


        # the way of solving this quesiont is that we want each word to have the same amount of letters for each part. 

        # so for example, in words = ["abc","aabc","bc"]


        # here we  have a = 3, b = 3, c = 3. because this matches it means that we can make similar words all across. as long as the size of the list is matches the size of the words, and it can be divisible by that too. 

        # so we could have a = 6 , b = 6, c = 6 

        # and the way we can see if this is true is by doing 


        # if count % lenght == 0, it means that they were divisible, if not it would come out as falase 


        # the way we will count them is we are going to use a hashmap to count them 

        length = len(words)

        count = {}

        for word in words: 

            for char in word: 

                # so right now we have each letter for each word 

                count[char] = count.get(char, 0) + 1   # this is a knwon way of checking if the words has been there before, if it is, it will return that value, if it isnt it will be 0, and then we add + 1


                # so after the fact the count will look like this: 


        # count = {a : 3, b : 3, c: 3}



        # now we see if the total count 

        

        for count in count.values(): 

            if count % length == 0: 

                continue 

            else: 

                return False 

        return True




        