class Twitter:

    def __init__(self):
        self.timer = 0 # we are going to set the timer to 0 
        self.tweets = defaultdict(list) # defaultdisct is very important becasue is we dont have any key for tweet, it will automatically create a list for us
        self.followers = defaultdict(set) # if there isnt a key then we will get a set instead, a set is used so that all the follower have unique ids 


    def postTweet(self, userId: int, tweetId: int) -> None:
        # we will get the user id,each tweetId is unique
        # for posting tweets what we want is

        # we want to have the userID, so that each user ID would have their own place to send tweets, and then we want to put time into it
        # and also tweetID, so we want to create a tuple (timer, tweetId) 

        # it would look like this: 

        # 1 = {0, 3}
        # 4 = {-1, 5}  it should look like something like this 
        # 2 = {-2, 2} 

        # keep in mind that our times will be set in negatives, becasue later we are going to use that in order to get the max_heap, and have the most recent post 

        self.tweets[userId].append((self.timer, tweetId)) # we use append that way we can keep track of multiple values for tweets, if i use =, then it would repalce them
        self.timer = self.timer - 1 
        # we set it negative, becasue we want to organize them in a max_heap, and for that we need use -, and a min_heap, otherwise it woudlnt work




    def getNewsFeed(self, userId: int) -> List[int]:
        #return a list of the 10 most recent tweet, has to be by people they are following or thmeslefs,
        # should be ordered from most recent to least recent 

        res = [] # this will hold our final 10 tweets ids 
        max_heap = [] # this will be our waiting room for the most recent tweets 
        self.followers[userId].add(userId)  # we are going to follow ourselves, to make this code much easier 

        for followeeId in self.followers[userId]: # we are going to see all of our followers, 
            if followeeId in self.tweets: # we are going to see in our followers, and if in our followers there is someone that wrote a tweet
                index = len(self.tweets[followeeId]) - 1 # okay this might be complicated, but when we have this for example: 
                 # 1 = {0, 3} , it could happen that the same user posts something else, is very common, and possible so if that where to happened, then we would get
                 # 1 = {[0,3], [-2, 4]} and if they post another feewd
                 # 1 = {[0,3], [-2, 4], [-4, 3]} and so on and on, so when we say len(self.tweets[followeeid]) we are asking for the lenght of the tweets, in this example is 3
                # but for the example that we had, is only 1 

                # 1 = {0, 3} === this would be the index ===== 1 

                #  1 = {[0,3], [-2, 4], [-4, 3]} ===== this would be the index ==== 3


                # we do the -1, so that we can have that number in the index 

                # the index will always give us the last of tweeted 

                time, tweetId = self.tweets[followeeId][index]

                # ok this line is also super complicated, but what we are doing here 
                # is we want to make sure that we get the last index of our tweetid
                # and we separate values, so for this exampe we have 

                # this user that tweated this :

                #  1 = {[0,3], [-2, 4], [-4, 3]} 

                # so self.tweets[followeeid][index] = self.tweet[1][2]. so the idea, is 1, and the index is 2

                # so that would be [-4, 3] 

                # that means that: 

                # time = -4 
                # tweetid = 3 

                max_heap.append((time, tweetId, followeeId, index - 1))


                # what is happening here is also super complicated. but what is happening is we are seeting the max_heap
                # in order, so that we can have the time the one deciding what value goes first, and if the value is -10 for example that means that it would be on the top waiting
                # so is going to save their tweet id, the followeeidm and their index, has to be one less, becauyse if we already looked for this user
                # then we have to look at index - 1, the one before this one 
                
        heapq.heapify(max_heap)    # this will set our heap in order 

        while max_heap and len(res) < 10: # while the result doesnt have more than the 10 tweets , and max_heap still has values we will keep on going
            time, tweetId, followeeId, next_index = heapq.heappop(max_heap) # we unpack all the values, and 
            # and we take the most recent one that will be on the top of the value 
            # and we then put his id on the result 
            res.append(tweetId)

            # notice how we set our next_index as 1.. remeber that we set that before 

            if next_index >= 0: # if the nex_index is bigger or equal to 0, we can use that next indext to grap the next tweer 
                next_time, next_tweetId = self.tweets[followeeId][next_index] # use the next index to check for that to see if we can find it being smaller 

                # we will also save the time of that, and the next_tweet id, to save this into the heap 

                heapq.heappush(max_heap,(next_time, next_tweetId, followeeId, next_index - 1))
        
        return res 


 
    def follow(self, followerId: int, followeeId: int) -> None:
        # the user with the followerId, is trying to to follow the user with id followeed
        if followerId != followeeId: # we prevent ourselves from following ourselves 
            self.followers[followerId].add(followeeId) # make the follower follow his idol
        
        # we use add becasue is a set, and in a set, we want to keep add, that way all the values are unique 

        # it will look like this: 

        # 3 = {5, 2} # the user 3, is following 5, 2  

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.followers[followerId]: # if the follow is on your id's, go ahead and erase it 

        # user with followerId unfollows the user with ID followeid
            self.followers[followerId].remove(followeeId) # remove the follower you want 