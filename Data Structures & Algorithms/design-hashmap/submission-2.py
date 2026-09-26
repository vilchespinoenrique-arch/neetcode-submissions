class MyHashMap:

    def __init__(self):
        self.size_bucket = 1000

        self.bucket = []

        for _ in range(self.size_bucket):
            self.bucket.append([])
        

    def put(self, key: int, value: int) -> None:
        # this is to put in the keys 
        index = key % self.size_bucket

        for i,pair in enumerate(self.bucket[index]):
        
            if pair[0] == key: # if the key is already in the bucket index.. then we can append another one 

                self.bucket[index][i][1] = value
                return

        # if note we will create a new key 

        self.bucket[index].append([key,value])

    def get(self, key: int) -> int:
        
        index = key % self.size_bucket

        for i, pair in enumerate(self.bucket[index]):

            if pair[0] == key:
                return pair[1]
            
            
        
        return -1 

        

    def remove(self, key: int) -> None:

        index = key % self.size_bucket

        
        for i, pair in enumerate(self.bucket[index]):
            if pair[0] == key:

                self.bucket[index].pop(i) # remove the first element. mayber we nee to erase more thant 1

                return 

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)