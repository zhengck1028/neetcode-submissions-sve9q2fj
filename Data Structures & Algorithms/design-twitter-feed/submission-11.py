class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followers[userId].add(userId)
        for i in self.followers[userId]:
            j = len(self.tweets[i]) - 1
            if self.tweets[i]:
                heapq.heappush(heap, [self.tweets[i][j][0], i, j, self.tweets[i][j][1]])
        while heap and len(res) < 10:
            t, i, j, tw = heapq.heappop(heap)
            res.append(tw)
            if j - 1 >= 0:
                heapq.heappush(heap, [self.tweets[i][j-1][0], i, j-1,self.tweets[i][j-1][1]])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
