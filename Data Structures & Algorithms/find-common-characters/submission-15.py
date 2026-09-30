class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        


        hashmap = {}



        for char in words[0]:

            hashmap[char] = hashmap.get(char, 0 ) + 1 


        

        # now we compare one by one, and we get the minimum between them 



        for word in words:

            new_hashmap = {}


            for c in word: 

                new_hashmap[c] = new_hashmap.get(c, 0) + 1



            for r in hashmap: 

                hashmap[r] = min(hashmap[r], new_hashmap.get(r, 0))


            # now hashmpa will have the minimum patter saved

            # so like this 


            # e : 1, l: 2 


        result = []


        for key, value in hashmap.items():

            for i in range(0, value):

                result.append(key)


        return result 
