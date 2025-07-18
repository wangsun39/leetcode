# 表：Activity
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | session_id    | int     |
# | activity_date | date    |
# | activity_type | enum    |
# +---------------+---------+
# 该表没有包含重复数据。
# activity_type 列是 ENUM(category) 类型， 从 ('open_session'， 'end_session'， 'scroll_down'， 'send_message') 取值。
# 该表记录社交媒体网站的用户活动。
# 注意，每个会话只属于一个用户。
#
#
# 编写解决方案，统计截至 2019-07-27（包含2019-07-27），近 30 天的每日活跃用户数（当天只要有一条活动记录，即为活跃用户）。
#
# 以 任意顺序 返回结果表。
#
# 结果示例如下。
#
#
#
# 示例 1:
#
# 输入：
# Activity table:
# +---------+------------+---------------+---------------+
# | user_id | session_id | activity_date | activity_type |
# +---------+------------+---------------+---------------+
# | 1       | 1          | 2019-07-20    | open_session  |
# | 1       | 1          | 2019-07-20    | scroll_down   |
# | 1       | 1          | 2019-07-20    | end_session   |
# | 2       | 4          | 2019-07-20    | open_session  |
# | 2       | 4          | 2019-07-21    | send_message  |
# | 2       | 4          | 2019-07-21    | end_session   |
# | 3       | 2          | 2019-07-21    | open_session  |
# | 3       | 2          | 2019-07-21    | send_message  |
# | 3       | 2          | 2019-07-21    | end_session   |
# | 4       | 3          | 2019-06-25    | open_session  |
# | 4       | 3          | 2019-06-25    | end_session   |
# +---------+------------+---------------+---------------+
# 输出：
# +------------+--------------+
# | day        | active_users |
# +------------+--------------+
# | 2019-07-20 | 2            |
# | 2019-07-21 | 2            |
# +------------+--------------+
# 解释：注意非活跃用户的记录不需要展示。

import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    selected = activity[(activity['activity_date'] >= '2019-06-28')&(activity['activity_date'] <= '2019-07-27')]
    grouped = selected.groupby('activity_date')
    ans = grouped['user_id'].nunique().reset_index(name='active_users')
    ans.rename(columns={'activity_date': 'day'}, inplace=True)
    return ans


data = [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'], [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'], [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'], [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'], [3, 2, '2019-07-21', 'end_session'], [4, 3, '2019-06-25', 'open_session'], [4, 3, '2019-06-25', 'end_session']]
activity = pd.DataFrame(data, columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype({'user_id':'Int64', 'session_id':'Int64', 'activity_date':'datetime64[ns]', 'activity_type':'object'})


print(user_activity(activity))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select activity_date as day, count(distinct user_id) active_users from Activity where activity_date between '2019-06-28' and '2019-07-27' group by activity_date;



