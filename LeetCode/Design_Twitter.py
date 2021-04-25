# Leetcode
# https://leetcode.com/problems/design-twitter/


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news_feed = []
        count = 0
        for i in self.tweets[::-1]:
            if userId == i[0] or (userId in self.follows and i[0] in self.follows[userId]):
                news_feed.append(i[1])
                count += 1
                if count == 10:
                    break
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        temp = self.follows.get(followerId, set())
        temp.add(followeeId)
        self.follows[followerId] = temp

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        temp = self.follows.get(followerId, set())
        if followeeId in temp:
            temp.remove(followeeId)
            self.follows[followerId] = temp


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
