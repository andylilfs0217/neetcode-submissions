from collections import defaultdict

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.following[userId].add(userId)
        self.time -= 1
        heapq.heappush(self.tweets[userId], (self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        followees = self.following[userId]
        temp_feed = []
        for followee in followees:
            followee_tweets = heapq.nsmallest(10, self.tweets[followee])
            for tweet in followee_tweets:
                heapq.heappush(temp_feed, tweet)
            temp_feed = heapq.nsmallest(10, temp_feed)
        feed = [tweet for _, tweet in temp_feed]
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        self.following[followerId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
