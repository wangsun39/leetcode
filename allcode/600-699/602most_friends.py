# RequestAccepted 表：
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | requester_id   | int     |
# | accepter_id    | int     |
# | accept_date    | date    |
# +----------------+---------+
# (requester_id, accepter_id) 是这张表的主键(具有唯一值的列的组合)。
# 这张表包含发送好友请求的人的 ID ，接收好友请求的人的 ID ，以及好友请求通过的日期。
#
#
# 编写解决方案，找出拥有最多的好友的人和他拥有的好友数目。
#
# 生成的测试用例保证拥有最多好友数目的只有 1 个人。
#
# 查询结果格式如下例所示。
#
#
#
# 示例 1：
#
# 输入：
# RequestAccepted 表：
# +--------------+-------------+-------------+
# | requester_id | accepter_id | accept_date |
# +--------------+-------------+-------------+
# | 1            | 2           | 2016/06/03  |
# | 1            | 3           | 2016/06/08  |
# | 2            | 3           | 2016/06/08  |
# | 3            | 4           | 2016/06/09  |
# +--------------+-------------+-------------+
# 输出：
# +----+-----+
# | id | num |
# +----+-----+
# | 3  | 3   |
# +----+-----+
# 解释：
# 编号为 3 的人是编号为 1 ，2 和 4 的人的好友，所以他总共有 3 个好友，比其他人都多。
#
#
# 进阶：在真实世界里，可能会有多个人拥有好友数相同且最多，你能找到所有这些人吗？

import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df1 = request_accepted[['requester_id']].copy()
    df1.rename(columns={'requester_id': 'id'}, inplace=True)
    df2 = request_accepted[['accepter_id']].copy()
    df2.rename(columns={'accepter_id': 'id'}, inplace=True)
    df = pd.concat([df1, df2], ignore_index=True)
    grouped = df.groupby('id')
    g = grouped.size().reset_index(name='num')
    g = g[g['num'].max() == g['num']]
    print(g)

    return g



data = [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']]
request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype({'requester_id':'Int64', 'accepter_id':'Int64', 'accept_date':'datetime64[ns]'})


print(most_friends(request_accepted))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select customer_number from (select customer_number, count(1) as cnt from Orders group by customer_number order by cnt desc limit 1) a;

