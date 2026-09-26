class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        hashmap = {} 

        good = False 

        result = []


        for char in chars:


            hashmap[char] = hashmap.get(char, 0) + 1


            # the hashmap will look like this: 


            # hashmap = {a: 2, t: 1, c: 1, h: 1} 




        


        for word in words: 

            copy_of_hashmap = hashmap.copy()

            for char in word: 

                if char in copy_of_hashmap: 

                    good = True 

                    copy_of_hashmap[char] = copy_of_hashmap[char] - 1

                    if copy_of_hashmap[char] == 0: 
                         
                         del copy_of_hashmap[char]
                
                else: 

                    good = False 

                    break 

            if good: 

                result.append(word)

        
        total = 0 


        for word in result: 

            total = total + len(word) 

        return total 


                        


                   

