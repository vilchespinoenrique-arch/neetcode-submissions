class Logger:

    def __init__(self):

        # okay the first thing we have to understand about this question is '

        self.hashmap = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:



        if message not in self.hashmap or timestamp >= self.hashmap[message] + 10:

            self.hashmap[message] = timestamp

            return True 


        else: 

            return False 
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
