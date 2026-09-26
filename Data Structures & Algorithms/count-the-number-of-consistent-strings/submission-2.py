class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        

        
        my_set = set(allowed)  # lets go ahead and have 

        
        result = []



        for word in words: 

            good = False

            for char in word: 

                if char in my_set: 

                    good = True 

                else: 

                    good = False

                    break 

            if good: 

                result.append(word)


        return len(result)
            

