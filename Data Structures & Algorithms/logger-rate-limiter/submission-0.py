class Logger:

    def __init__(self):
        
        self.hashmap = {}

        # we want to set the hashmap here, becasue when we create each new object, with loogger as you see in the example we want logger to be able to survive. survive between calls 

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        

        # in print messages in here we are going to set all the things that do constantly change and that dont need to follow calls, becasue they are different each call, 

        # that would be the timestamp and the message 

        # keep in mind that we dont need a for loop because all the calls will be coming from the new object when they call the function 


        # For a visual to make simplier on me, what the hashmpa will look like at first will be like this 


        # hasmap = { foo : 1, } the first one it iwll see 

        

        if message not in self.hashmap or timestamp >= self.hashmap[message] + 10: 

            self.hashmap[message] = timestamp

            return True 
        

        else: 
            
            return False 
            
          
        
        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
