# 表：UserActivity
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | user_id          | int     |
# | activity_date    | date    |
# | activity_type    | varchar |
# | activity_duration| int     |
# +------------------+---------+
# (user_id, activity_date, activity_type) 是这张表的唯一主键。
# activity_type 是('free_trial', 'paid', 'cancelled')中的一个。
# activity_duration 是用户当天在平台上花费的分钟数。
# 每一行表示一个用户在特定日期的活动。
# 订阅服务想要分析用户行为模式。公司提供7天免费试用，试用结束后，用户可以选择订阅 付费计划 或 取消。编写解决方案：
#
# 查找从免费试用转为付费订阅的用户
# 计算每位用户在 免费试用 期间的 平均每日活动时长（四舍五入至小数点后 2 位）
# 计算每位用户在 付费 订阅期间的 平均每日活动时长（四舍五入到小数点后 2 位）
# 返回结果表以 user_id 升序 排序。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# UserActivity 表：
#
# +---------+---------------+---------------+-------------------+
# | user_id | activity_date | activity_type | activity_duration |
# +---------+---------------+---------------+-------------------+
# | 1       | 2023-01-01    | free_trial    | 45                |
# | 1       | 2023-01-02    | free_trial    | 30                |
# | 1       | 2023-01-05    | free_trial    | 60                |
# | 1       | 2023-01-10    | paid          | 75                |
# | 1       | 2023-01-12    | paid          | 90                |
# | 1       | 2023-01-15    | paid          | 65                |
# | 2       | 2023-02-01    | free_trial    | 55                |
# | 2       | 2023-02-03    | free_trial    | 25                |
# | 2       | 2023-02-07    | free_trial    | 50                |
# | 2       | 2023-02-10    | cancelled     | 0                 |
# | 3       | 2023-03-05    | free_trial    | 70                |
# | 3       | 2023-03-06    | free_trial    | 60                |
# | 3       | 2023-03-08    | free_trial    | 80                |
# | 3       | 2023-03-12    | paid          | 50                |
# | 3       | 2023-03-15    | paid          | 55                |
# | 3       | 2023-03-20    | paid          | 85                |
# | 4       | 2023-04-01    | free_trial    | 40                |
# | 4       | 2023-04-03    | free_trial    | 35                |
# | 4       | 2023-04-05    | paid          | 45                |
# | 4       | 2023-04-07    | cancelled     | 0                 |
# +---------+---------------+---------------+-------------------+
# 输出：
#
# +---------+--------------------+-------------------+
# | user_id | trial_avg_duration | paid_avg_duration |
# +---------+--------------------+-------------------+
# | 1       | 45.00              | 76.67             |
# | 3       | 70.00              | 63.33             |
# | 4       | 37.50              | 45.00             |
# +---------+--------------------+-------------------+
# 解释：
#
# 用户 1:
# 体验了 3 天免费试用，时长分别为 45，30 和 60 分钟。
# 平均试用时长：(45 + 30 + 60) / 3 = 45.00 分钟。
# 拥有 3 天付费订阅，时长分别为 75，90 和 65分钟。
# 平均花费时长：(75 + 90 + 65) / 3 = 76.67 分钟。
# 用户 2:
# 体验了 3 天免费试用，时长分别为 55，25 和 50 分钟。
# 平均试用时长：(55 + 25 + 50) / 3 = 43.33 分钟。
# 没有转为付费订阅（只有 free_trial 和 cancelled 活动）。
# 未包含在输出中，因为他未转换为付费用户。
# 用户 3:
# 体验了 3 天免费试用，时长分别为 70，60 和 80 分钟。
# 平均试用时长：(70 + 60 + 80) / 3 = 70.00 分钟。
# 拥有 3 天付费订阅，时长分别为 50，55 和 85 分钟。
# 平均花费时长：(50 + 55 + 85) / 3 = 63.33 分钟。
# 用户 4:
# 体验了 2 天免费试用，时长分别为 40 和 35 分钟。
# 平均试用时长：(40 + 35) / 2 = 37.50 分钟。
# 在取消前有 1 天的付费订阅，时长为45分钟。
# 平均花费时长：45.00 分钟。
# 结果表仅包括从免费试用转为付费订阅的用户（用户 1，3 和 4），并且以 user_id 升序排序。

import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    user_activity = user_activity[user_activity['activity_type']!='cancelled']
    df = (
        user_activity
        .groupby(['user_id', 'activity_type'], dropna=False)  # 显式保留 NaN
        .agg(
            avg=('activity_duration', 'mean')
        )
    ).reset_index()

    ans = pd.pivot_table(df, index='user_id', columns='activity_type', values='avg')



    return ans






data = [[1, '2023-01-01', 'free_trial', 45], [1, '2023-01-02', 'free_trial', 30], [1, '2023-01-05', 'free_trial', 60], [1, '2023-01-10', 'paid', 75], [1, '2023-01-12', 'paid', 90], [1, '2023-01-15', 'paid', 65], [2, '2023-02-01', 'free_trial', 55], [2, '2023-02-03', 'free_trial', 25], [2, '2023-02-07', 'free_trial', 50], [2, '2023-02-10', 'cancelled', 0], [3, '2023-03-05', 'free_trial', 70], [3, '2023-03-06', 'free_trial', 60], [3, '2023-03-08', 'free_trial', 80], [3, '2023-03-12', 'paid', 50], [3, '2023-03-15', 'paid', 55], [3, '2023-03-20', 'paid', 85], [4, '2023-04-01', 'free_trial', 40], [4, '2023-04-03', 'free_trial', 35], [4, '2023-04-05', 'paid', 45], [4, '2023-04-07', 'cancelled', 0]]
user_activity = pd.DataFrame(data, columns=['user_id', 'activity_date', 'activity_type', 'activity_duration'])

print(analyze_subscription_conversion(user_activity))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select * from (
# select user_id,
#     round(avg(case when activity_type='free_trial' then activity_duration end), 2) trial_avg_duration,
#     round(avg(case when activity_type='paid' then activity_duration end), 2) paid_avg_duration
# from UserActivity where activity_type in ('free_trial', 'paid') group by user_id)
# where paid_avg_duration>1 order by user_id;


