class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        

        # we are going to have 2 different list, one will hold the indexes of the word1, 

        # and the other list will hold the indexes of the other word 



        list1 = [] 

        list2 = []


        for i in range(0, len(wordsDict)): 


            if wordsDict[i] == word1: 

                list1.append(i)


            elif wordsDict[i] == word2: 

                list2.append(i)


            
            else: 

                continue 



        # now in list 1 we have the indexes of the first word and in list2 we have the indexes of word2 


        # so now we need to find the smalles difference between this 2 



        # list1 = [0]     list2 = [3]


        i = 0 

        j = 0 

        difference = 10000

        while j < len(list1) and i < len(list2): 

            for i in range(0, len(list2)):

                difference = min(difference, abs(list1[j] - list2[i]))

    

            j += 1


        return difference






            


