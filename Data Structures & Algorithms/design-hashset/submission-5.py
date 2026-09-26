class MyHashSet:

    def __init__(self):
        self.size_bucket = 1000

        self.bucket = []
        for _ in range(self.size_bucket):
            self.bucket.append([])

        # in here we create the bucker that will hold our values 
    
    def add(self, key: int) -> None:

        index = key % self.size_bucket # this is a classic way to get the index, we want the index, so that we can put the keys in a place

        if key not in self.bucket[index]: # if that key is not in there, then we can go ahead and added

            self.bucket[index].append(key)
        
        

    def remove(self, key: int) -> None:
        index = key % self.size_bucket

        if key in self.bucket[index]:
            self.bucket[index].remove(key)

        

    def contains(self, key: int) -> bool:
        
        index = key % self.size_bucket

        if key in self.bucket[index]:
            return True 
        
        else:
            return False 

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# for this question we have to keep in mind that a hashsets, only keep keys inside, it doesnt keep values like a hashmap does 