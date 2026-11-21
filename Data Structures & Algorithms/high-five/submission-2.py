from collections import defaultdict

from typing import List 

import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:



        heaps = defaultdict(list)


        for index, scores in items: 


            heapq.heappush(heaps[index], scores) 


            if len(heaps[index]) > 5: 

                heapq.heappop(heaps[index])


        
        result = []


        for index in sorted(heaps): 


            average = sum(heaps[index]) // 5 


            result.append([index, average])
        

        return result 


        