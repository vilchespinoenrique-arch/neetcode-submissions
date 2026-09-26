class Solution:
    def isValid(self, s: str) -> bool:
        


        # input s = "([{}])", then this would be correct 

        # this question is perfect for stack 

        # becasue in stack we have first items that come, will stay there longer, and the ones coming in will leave inmediately
        # just like a panckake 

        # with this idea, something you can do is, you can use a dictionart to match the different one. and matched so that the last element we got we can compare it to the last one we had and if is a closing bracket where, where that closed bracket doesnt mathc the last one, then we can return false inmediately 

        dictionary = {')': '(',   ']':'[',   '}':'{' } # this dictionary, we will have the key as the close bracket, and when we get a close bracket, if that close bracket matches the open bracket that we had last, then we will be good and we can remove it 

        hold_brackets = []
        
        for char in s: 
            
            if char in dictionary.values():  # in here i want to say if there is a value inside the dictionary, that matches.. then go ahead and put in the list
                hold_brackets.append(char)

                # lets think that we have a open bracket = [( ]
                # and the next one is a close bracket = )





            elif char in dictionary: 
                
                if not hold_brackets or dictionary[char] != hold_brackets[-1]:
                    return False
            
                hold_brackets.pop()

                # checj if this works 

                #dictionary[}]
            else: 
                continue 

        if len(hold_brackets) == 0:
            return True 
        else: 
            return False
                