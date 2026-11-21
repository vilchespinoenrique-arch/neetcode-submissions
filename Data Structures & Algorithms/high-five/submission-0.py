import heapq

from collections import defaultdict

from typing import List



class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        

        # for this question the first thing is to understnad defaultdic 

        # when we say heap = defaultdic(list) -> this means that we just create a diccionary where it will take values as list,

        # if we change list to int, it would have the values an int, for the starting ones, then we can change it 


        # heap will look like this 


        # heap = {1: [91, 92]} ... etc 



        heaps = defaultdict(list)


        # now that we have our heaps, we can start using the index to create the different heaps 


        for index, score in items: 


            heapq.heappush(heaps[index], score)  # here each score, will go depending on the index 

            if len(heaps[index]) > 5: 

                heapq.heappop(heaps[index]) # this guarantees that we only have the top 5 scores 


        
        # we now have the heaps created 


        result = []


        for index in sorted(heaps): 

            average = sum(heaps[index]) // 5 

            result.append([index, average])


        return result 






