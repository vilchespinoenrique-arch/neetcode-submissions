from collections import defaultdict
import heapq
from typing import List 
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        

        # the first idea is to create different heaps, however we want to do that using a dictionary.

        # we want to use a dictionary becasue we will use the index as the key to enter the heap 


        heaps = defaultdict(list)


        for index, scores in items: 

            heapq.heappush(heaps[index], scores)  # so think about this, the first argument is where we go, in here we will be going to that dictionary, where the key is the index, and there we say the scores. with the heap properties 


            if len(heaps[index]) > 5: 

                heapq.heappop(heaps[index])


        
        result = []


        for index in sorted(heaps): 

            average = sum(heaps[index]) // 5 

            result.append([index, average])

        return result 



