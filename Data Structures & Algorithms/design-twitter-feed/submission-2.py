class Twitter:

    def __init__(self):
        self.counter = 0
        self.followMap = {}
        self.tweetMap = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = [[-self.counter, tweetId]]
        else:
            self.tweetMap[userId].append([-self.counter, tweetId])

        self.counter += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        list_of_tweets = []

        # Get all the tweets by the user
        if userId in self.tweetMap:
            for tweet in self.tweetMap[userId]:
                list_of_tweets.append(tweet)

        # Get all the tweets by all the users that this user follows:
        if userId in self.followMap:
            for followeeId in self.followMap[userId]:
                for tweet in self.tweetMap[followeeId]:
                    list_of_tweets.append(tweet)

        heapq.heapify(list_of_tweets)
        res = []

        while len(res) != 10 and len(list_of_tweets) != 0:
            res.append(list_of_tweets[0][1])
            heapq.heappop(list_of_tweets)

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()

        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
        
