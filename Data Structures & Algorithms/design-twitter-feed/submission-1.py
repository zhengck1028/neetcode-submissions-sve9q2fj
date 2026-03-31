class Twitter:
    import heapq
    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        Ids = self.followers[userId]
        Ids.add(userId)
        minheap = []
        for i in Ids:
            if self.tweets[i]:
                index = len(self.tweets[i]) - 1
                heapq.heappush(minheap, [self.tweets[i][index][0], i, self.tweets[i][index][1], index])
        while len(res) < 10 and minheap:
            t, Id, tw, index = heapq.heappop(minheap)
            res.append(tw)
            if index > 0:
                heapq.heappush(minheap, [self.tweets[Id][index-1][0], Id, self.tweets[Id][index-1][1], index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
