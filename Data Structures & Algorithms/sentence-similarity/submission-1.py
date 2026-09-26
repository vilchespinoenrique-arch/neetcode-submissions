class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        

        # the first thing we are going to check is if sentecen 1 is the same lenght as sentence 2, becasue if it isnt. then there is not much to discussed here, and this will become false inmediately 


        if len(sentence1) != len(sentence2):

            return False 

        

        tuples = set() 


        for word1, word2 in similarPairs: # we similar pairs are a list, that has a list withing itself, so we can use that to create our tuples, that we will later compared 

            tuples.add((word1,word2))

            tuples.add((word2,word1)) 

            # we will have them both ways just in case. but if you are curious. this is how that look likes


            # tuples = { ("great", "fine"), ("fine", "great"), ("drama", "acting"), ("acting", "drama") } and it will keep going but i didnt want to do all of them 


        

        # now we can compare with the sentences. but first things first we need to compbine them into a zip 


        for check1, check2 in zip(sentence1, sentence2): 

            if check1 != check2 and (check1, check2) not in tuples: 
                return False 


        return True 
