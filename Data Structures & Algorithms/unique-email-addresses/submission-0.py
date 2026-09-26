class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        

        # i didnt know this, but we can use something called split() 

        # where we put the char we want to split in the function split 


        # there also something called replace, which if i see that specific char, i can replace it however I want 


        unique = set()
        
        
        for email in emails: 

            local, domain = email.split('@') # here local and domain will be splitted in half 

            # local = test.email+alex

            # domain = neetcode.com 


            local = local.split('+')[0] # this is sayinh that if we see a local that has a + 

            # split it and keep the part before the + sign, if we want the things after the 

            # + signs we would use [1]

            local = local.replace('.', '') # this replace function is saying, that if we see a dot, go ahead and replace it for noting. 


            # so if we have 

            # local = test.email -> testemail 


            unique.add(local + '@' + domain) 


        return len(unique)
            