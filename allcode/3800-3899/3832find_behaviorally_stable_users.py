# 表：activity
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | user_id      | int     |
# | action_date  | date    |
# | action       | varchar |
# +--------------+---------+
# (user_id, action_date, action) 是这张表的主键（值互不相同）。
# 每一行代表一个用户在特定日期执行的具体操作。
# 根据以下定义，编写一个解决方案来识别 行为稳定的用户：
#
# 一个用户如果存在一个 连续至少 5 天的行为序列满足以下条件，则认为他是 行为稳定 的：
# 该用户在该期间 每天只执行了一个操作。
# 这些连续的日子里，操作都是相同的。
# 如果一个用户有多个符合条件的序列，只考虑 最长 的那条序列。
# 返回结果表按 streak_length 降序 排序，然后按 user_id 升序 排序。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# activity 表：
#
# +---------+-------------+--------+
# | user_id | action_date | action |
# +---------+-------------+--------+
# | 1       | 2024-01-01  | login  |
# | 1       | 2024-01-02  | login  |
# | 1       | 2024-01-03  | login  |
# | 1       | 2024-01-04  | login  |
# | 1       | 2024-01-05  | login  |
# | 1       | 2024-01-06  | logout |
# | 2       | 2024-01-01  | click  |
# | 2       | 2024-01-02  | click  |
# | 2       | 2024-01-03  | click  |
# | 2       | 2024-01-04  | click  |
# | 3       | 2024-01-01  | view   |
# | 3       | 2024-01-02  | view   |
# | 3       | 2024-01-03  | view   |
# | 3       | 2024-01-04  | view   |
# | 3       | 2024-01-05  | view   |
# | 3       | 2024-01-06  | view   |
# | 3       | 2024-01-07  | view   |
# +---------+-------------+--------+
# 输出：
#
# +---------+--------+---------------+------------+------------+
# | user_id | action | streak_length | start_date | end_date   |
# +---------+--------+---------------+------------+------------+
# | 3       | view   | 7             | 2024-01-01 | 2024-01-07 |
# | 1       | login  | 5             | 2024-01-01 | 2024-01-05 |
# +---------+--------+---------------+------------+------------+
# 解释：
#
# 用户 1：
# 从 2024 年 1 月 1 日至 2024 年 1 月 5 日连续五天执行 login 操作
# 每一天都恰好有一个操作，且操作相同
# 连续长度 = 5（满足最小要求）
# 行动在 2024-01-06 发生变化，结束连续计数
# 用户 2：
# 只连续执行了 4 天 click 操作
# 不满足最小连续计数 5 天的要求
# 从结果排除
# 用户 3：
# 连续 7 天执行了 view 操作
# 这是此用户的最长有效序列
# 包含在结果中
# 结果表按 streak_length 降序排序，然后按 user_id 升序排序。

import pandas as pd
from leetcode.allcode.competition.mypackage import *

def find_behaviorally_stable_users(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=['user_id', 'action_date'], inplace=True)
    activity['date_time'] = pd.to_datetime(activity['action_date'])

    def proc(g):
        rows = []

        for row in g.itertuples(index=False, name='Row'):
            rows.append([row.action_date, row.action, row.date_time])

        start = 0
        mx = 0
        mx_start = 0
        for i, [date, action, date_time] in enumerate(rows):
            if i and ((date_time - rows[i - 1][2]) / pd.Timedelta(days=1) != 1 or action != rows[i - 1][1]):
                start = i
            if i - start >= 4:
                if i - start + 1 > mx:
                    mx_start = start
                    mx = i - start + 1
        if mx == 0: return

        return pd.Series({'action': rows[mx_start][1], 'streak_length': mx,
                          'start_date': rows[mx_start][0], 'end_date': rows[mx_start + mx - 1][0]})


    ans = activity.groupby(by='user_id')[['action_date', 'action', 'date_time']].apply(func=proc).reset_index()
    if len(ans) == 0:
        return pd.DataFrame([], columns=[
            "user_id",
            "action",
            "streak_length",
            'start_date',
            'end_date'
        ])
    ans = ans[ans['action'].notna()]
    return ans.sort_values(by=['streak_length', 'user_id'], ascending=[False, True])




data = [[1, '2024-01-01', 'login'], [1, '2024-01-02', 'login'], [1, '2024-01-03', 'login'], [1, '2024-01-04', 'login'], [1, '2024-01-05', 'login'], [1, '2024-01-06', 'logout'], [2, '2024-01-01', 'click'], [2, '2024-01-02', 'click'], [2, '2024-01-03', 'click'], [2, '2024-01-04', 'click'], [3, '2024-01-01', 'view'], [3, '2024-01-02', 'view'], [3, '2024-01-03', 'view'], [3, '2024-01-04', 'view'], [3, '2024-01-05', 'view'], [3, '2024-01-06', 'view'], [3, '2024-01-07', 'view']]
activity = pd.DataFrame(data, columns=[
    "user_id",
    "action_date",
    "action"
])


print(find_behaviorally_stable_users(activity))

# -- Write your PostgreSQL query statement below

#


