class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_heap = []
        res = []
        self.followees[userId].add(userId)
        for i in self.followees[userId]:
            tws = self.tweets[i]
            if tws:
                last = len(tws) - 1
                tm, tw = tws[last]
                heapq.heappush(tweets_heap, [tm, tw, i, last])
        while tweets_heap and len(res) < 10:
            gtm, gtw, Id, idx = heapq.heappop(tweets_heap)
            res.append(gtw)
            if idx > 0:
                tm, tw = self.tweets[Id][idx - 1]
                heapq.heappush(tweets_heap, [tm, tw, Id, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
