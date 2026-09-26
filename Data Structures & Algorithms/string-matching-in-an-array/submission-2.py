class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:


        # the best thing that you can do for this question is using 2 pointer and go throught the array 

        # and now is not as good becasue it will be consider o(n^2), but that the best it can be 

        # 

        res = []

        for i in range(len(words)): 
            for j in range(len(words)): 

                if j != i and words[i] in words[j]: 

                    res.append(words[i])

                    break


        return res 
        