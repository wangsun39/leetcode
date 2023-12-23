# 一家社交媒体公司正试图通过分析特定时间段内出现的推文数量来监控其网站上的活动。这些时间段可以根据特定的频率（ 每分钟 、每小时 或 每一天 ）划分为更小的 时间段 。
#
#
#
# 例如，周期 [10,10000] （以 秒 为单位）将被划分为以下频率的 时间块 :
#
# 每 分钟 (60秒 块)： [10,69], [70,129], [130,189], ..., [9970,10000]
# 每 小时 (3600秒 块)：[10,3609], [3610,7209], [7210,10000]
# 每 天 (86400秒 块)： [10,10000]
# 注意，最后一个块可能比指定频率的块大小更短，并且总是以时间段的结束时间结束(在上面的示例中为 10000 )。
#
# 设计和实现一个API来帮助公司进行分析。
#
# 实现 TweetCounts 类:
#
# TweetCounts() 初始化 TweetCounts 对象。
# 存储记录时间的 tweetName (以秒为单位)。
# List<integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) 返回一个整数列表，表示给定时间 [startTime, endTime] （单位秒）和频率频率中，每个 时间块 中带有 tweetName 的 tweet 的数量。
# freq 是 “minute” 、 “hour” 或 “day” 中的一个，分别表示 每分钟 、 每小时 或 每一天 的频率。
#
#
# 示例：
#
# 输入：
# ["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
# [[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
#
# 输出：
# [null,null,null,null,[2],[2,1],null,[4]]
#
# 解释：
# TweetCounts tweetCounts = new TweetCounts();
# tweetCounts.recordTweet("tweet3", 0);
# tweetCounts.recordTweet("tweet3", 60);
# tweetCounts.recordTweet("tweet3", 10);                             // "tweet3" 发布推文的时间分别是 0, 10 和 60 。
# tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // 返回 [2]。统计频率是每分钟（60 秒），因此只有一个有效时间间隔 [0,60> - > 2 条推文。
# tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // 返回 [2,1]。统计频率是每分钟（60 秒），因此有两个有效时间间隔 1) [0,60> - > 2 条推文，和 2) [60,61> - > 1 条推文。
# tweetCounts.recordTweet("tweet3", 120);                            // "tweet3" 发布推文的时间分别是 0, 10, 60 和 120 。
# tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // 返回 [4]。统计频率是每小时（3600 秒），因此只有一个有效时间间隔 [0,211> - > 4 条推文。
#
#
# 提示：
#
# 0 <= time, startTime, endTime <= 109
# 0 <= endTime - startTime <= 104
# recordTweet 和 getTweetCountsPerFrequency，最多有 104 次操作。

from leetcode.allcode.competition.mypackage import *

class TweetCounts:

    def __init__(self):
        self.d = {}


    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.d:
            self.d[tweetName] = SortedList([time])
        else:
            self.d[tweetName].add(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.d:
            return [0]

        def calc(cycle):
            sl = self.d[tweetName]
            res = [0] * ((endTime - startTime + 1 + cycle - 1) // cycle)
            p1, p2 = sl.bisect_left(startTime), sl.bisect_right(endTime)
            if p1 == len(sl):
                return res
            start = sl[p1]
            cur = 0
            for t in range(p1, p2):
                if (sl[t] - startTime) // cycle == (start - startTime) // cycle:
                    cur += 1
                else:
                    res[(start - startTime) // cycle] = cur
                    start = sl[t]
                    cur = 1
                if t == p2 - 1:
                    res[(start - startTime) // cycle] = cur
            return res
        if freq == 'minute':
            return calc(60)
        elif freq == 'hour':
            return calc(3600)
        else:
            return calc(86400)





so = TweetCounts()
print(so.recordTweet("tweet3",0))
print(so.recordTweet("tweet3",60))
print(so.recordTweet("tweet3",10))
print(so.getTweetCountsPerFrequency("minute","tweet3",0,59))
print(so.getTweetCountsPerFrequency("minute","tweet3",0,60))
print(so.recordTweet("tweet3",120))
print(so.getTweetCountsPerFrequency("hour","tweet3",0,210))




