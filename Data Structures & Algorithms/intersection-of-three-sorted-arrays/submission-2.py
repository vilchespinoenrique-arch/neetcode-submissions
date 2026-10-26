from collections import Counter


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        
        
       


        count = Counter(arr1 + arr2 + arr3) 


        # counter works just like hashmap.get(char, 0) + 1. which is pretty neet because it means we can skip all of that and just import counter, which is pretty cool 



        result = []

        for key, value in count.items(): 


            if value == 3: 

                result.append(key)



            else: 

                continue 


        
        if result: 

            return result 


        else: 

            return []



        



            