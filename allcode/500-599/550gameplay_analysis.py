# Table: Activity
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | player_id    | int     |
# | device_id    | int     |
# | event_date   | date    |
# | games_played | int     |
# +--------------+---------+
# （player_id，event_date）是此表的主键（具有唯一值的列的组合）。
# 这张表显示了某些游戏的玩家的活动情况。
# 每一行是一个玩家的记录，他在某一天使用某个设备注销之前登录并玩了很多游戏（可能是 0）。
#
#
# 编写解决方案，报告在首次登录的第二天再次登录的玩家的 比率，四舍五入到小数点后两位。换句话说，你需要计算从首次登录日期开始至少连续两天登录的玩家的数量，然后除以玩家总数。
#
# 结果格式如下所示：
#
#
#
# 示例 1：
#
# 输入：
# Activity table:
# +-----------+-----------+------------+--------------+
# | player_id | device_id | event_date | games_played |
# +-----------+-----------+------------+--------------+
# | 1         | 2         | 2016-03-01 | 5            |
# | 1         | 2         | 2016-03-02 | 6            |
# | 2         | 3         | 2017-06-25 | 1            |
# | 3         | 1         | 2016-03-02 | 0            |
# | 3         | 4         | 2018-07-03 | 5            |
# +-----------+-----------+------------+--------------+
# 输出：
# +-----------+
# | fraction  |
# +-----------+
# | 0.33      |
# +-----------+
# 解释：
# 只有 ID 为 1 的玩家在第一天登录后才重新登录，所以答案是 1/3 = 0.33

import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    all_player_num = activity[['player_id']].drop_duplicates().shape[0]
    # print(all_player_num)
    grouped = activity.groupby('player_id')
    g1 = grouped['event_date'].min().reset_index()
    g1['second_day'] = g1['event_date'] + pd.DateOffset(days=1)
    # print(g1)
    g2 = pd.merge(activity, g1, left_on='player_id', right_on='player_id', how='inner')
    g2 = g2[g2['event_date_x'] == g2['second_day']]
    print(g2)
    selected_num = len(g2)
    return pd.DataFrame({'fraction':[round(selected_num / all_player_num, 2)]})
    # return pd.DataFrame([round(selected_num / all_player_num, 2)], columns=['fraction'])  // 两种写法



data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})



print(gameplay_analysis(activity))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# SELECT ROUND(
#     (
#         SELECT COUNT(*)
#         FROM activity a
#         JOIN (
#             SELECT player_id,
#                    MIN(event_date) AS first_day,
#                    MIN(event_date) + INTERVAL '1 day' AS second_day
#             FROM activity
#             GROUP BY player_id
#         ) b
#         ON a.player_id = b.player_id
#         WHERE a.event_date = b.second_day
#     ) /
#     (
#         SELECT COUNT(DISTINCT player_id)
#         FROM activity
#     )::NUMERIC,
#     2
# ) AS fraction;

