# 表：Tweets
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | tweet_id       | int     |
# | content        | varchar |
# +----------------+---------+
# 在 SQL 中，tweet_id 是这个表的主键。
# content 只包含字母数字字符，'!'，' '，不包含其它特殊字符。
# 这个表包含某社交媒体 App 中所有的推文。
#
#
# 查询所有无效推文的编号（ID）。当推文内容中的字符数严格大于 15 时，该推文是无效的。
#
# 以任意顺序返回结果表。
#
# 查询结果格式如下所示：
#
#
#
# 示例 1：
#
# 输入：
# Tweets 表：
# +----------+----------------------------------+
# | tweet_id | content                          |
# +----------+----------------------------------+
# | 1        | Vote for Biden                   |
# | 2        | Let us make America great again! |
# +----------+----------------------------------+
#
# 输出：
# +----------+
# | tweet_id |
# +----------+
# | 2        |
# +----------+
# 解释：
# 推文 1 的长度 length = 14。该推文是有效的。
# 推文 2 的长度 length = 32。该推文是无效的。

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['len']=tweets['content'].str.len()
    ans = tweets[tweets['len'] > 15][['tweet_id']]
    return ans


data = [[1, 'Let us Code'], [2, 'More than fifteen chars are here!']]
tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})


print(invalid_tweets(tweets))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select tweet_id from tweets where length(content) > 15;




