# 表： Followers
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | follower_id | int  |
# +-------------+------+
# (user_id, follower_id) 是这个表的主键（具有唯一值的列的组合）。
# 该表包含一个关注关系中关注者和用户的编号，其中关注者关注用户。
#
#
# 编写解决方案，对于每一个用户，返回该用户的关注者数量。
#
# 按 user_id 的顺序返回结果表。
#
# 查询结果的格式如下示例所示。
#
#
#
# 示例 1：
#
# 输入：
# Followers 表：
# +---------+-------------+
# | user_id | follower_id |
# +---------+-------------+
# | 0       | 1           |
# | 1       | 0           |
# | 2       | 0           |
# | 2       | 1           |
# +---------+-------------+
# 输出：
# +---------+----------------+
# | user_id | followers_count|
# +---------+----------------+
# | 0       | 1              |
# | 1       | 1              |
# | 2       | 2              |
# +---------+----------------+
# 解释：
# 0 的关注者有 {1}
# 1 的关注者有 {0}
# 2 的关注者有 {0,1}

import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    ans = (
        followers
        .groupby(['user_id'], dropna=False)  # 显式保留 NaN
        .agg(
            followers_count=('follower_id', 'size')
        )
    ).reset_index()
    ans.sort_values(by='user_id', inplace=True)
    return ans



data = [['0', '1'], ['1', '0'], ['2', '0'], ['2', '1']]
followers = pd.DataFrame(data, columns=['user_id', 'follower_id']).astype({'user_id':'Int64', 'follower_id':'Int64'})


print(count_followers(followers))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select user_id, count(1) followers_count from Followers group by user_id order by user_id;




