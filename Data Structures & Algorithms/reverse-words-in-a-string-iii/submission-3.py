class Solution:
    def reverseWords(self, s: str) -> str:
        pass


        # firs step - make the string into a list of words 


        word = s.split(" ")

        # now the word is looking like this 


        # # word = [ab, cd], we transfor the word into a list, and we split them where there was a space 


        result = []


        for char in word: 


            new_word = list(char)

            # now new word looks like this = 


            # new_word = ["a", "b"]

            left = 0 


            right = len(new_word) - 1


            while left <= right:


                new_word[left], new_word[right] = new_word[right], new_word[left] 


                left += 1 

                right -= 1 


            final = "".join(new_word) 


            result.append(final)


            final_1 = " ".join(result)


        return final_1




        