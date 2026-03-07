# 表：drivers
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | driver_id   | int     |
# | driver_name | varchar |
# +-------------+---------+
# driver_id 是这张表的唯一主键。
# 每一行都包含一个司机的信息。
# 表：trips
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | trip_id       | int     |
# | driver_id     | int     |
# | trip_date     | date    |
# | distance_km   | decimal |
# | fuel_consumed | decimal |
# +---------------+---------+
# trip_id 是这张表的唯一主键。
# 每一行表示一名司机完成的一次行程，包括该次行程行驶的距离和消耗的燃油量。
# 编写一个解决方案，通过 比较 司机在 上半年 和 下半年 的 平均燃油效率 来找出 燃油效率有所提高 的司机。
#
# 通过 distance_km / fuel_consumed 计算 每次 行程的 燃油效率。
# 上半年：一月到六月，下半年：七月到十二月
# 只包含在上半年和下半年都有行程的司机
# 通过（second_half_avg - first_half_avg）计算 提升效率。
# 将所有结果 四舍五入 到小数点后 2 位
# 返回结果表按提升效率 降序 排列，然后按司机姓名 升序 排列。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# drivers 表：
#
# +-----------+---------------+
# | driver_id | driver_name   |
# +-----------+---------------+
# | 1         | Alice Johnson |
# | 2         | Bob Smith     |
# | 3         | Carol Davis   |
# | 4         | David Wilson  |
# | 5         | Emma Brown    |
# +-----------+---------------+
# trips 表：
#
# +---------+-----------+------------+-------------+---------------+
# | trip_id | driver_id | trip_date  | distance_km | fuel_consumed |
# +---------+-----------+------------+-------------+---------------+
# | 1       | 1         | 2023-02-15 | 120.5       | 10.2          |
# | 2       | 1         | 2023-03-20 | 200.0       | 16.5          |
# | 3       | 1         | 2023-08-10 | 150.0       | 11.0          |
# | 4       | 1         | 2023-09-25 | 180.0       | 12.5          |
# | 5       | 2         | 2023-01-10 | 100.0       | 9.0           |
# | 6       | 2         | 2023-04-15 | 250.0       | 22.0          |
# | 7       | 2         | 2023-10-05 | 200.0       | 15.0          |
# | 8       | 3         | 2023-03-12 | 80.0        | 8.5           |
# | 9       | 3         | 2023-05-18 | 90.0        | 9.2           |
# | 10      | 4         | 2023-07-22 | 160.0       | 12.8          |
# | 11      | 4         | 2023-11-30 | 140.0       | 11.0          |
# | 12      | 5         | 2023-02-28 | 110.0       | 11.5          |
# +---------+-----------+------------+-------------+---------------+
# 输出：
#
# +-----------+---------------+------------------+-------------------+------------------------+
# | driver_id | driver_name   | first_half_avg   | second_half_avg   | efficiency_improvement |
# +-----------+---------------+------------------+-------------------+------------------------+
# | 2         | Bob Smith     | 11.24            | 13.33             | 2.10                   |
# | 1         | Alice Johnson | 11.97            | 14.02             | 2.05                   |
# +-----------+---------------+------------------+-------------------+------------------------+
# 解释：
#
# Alice Johnson (driver_id = 1):
# 上半年行程（一月到六月）：Feb 15 (120.5/10.2 = 11.81), Mar 20 (200.0/16.5 = 12.12)
# 上半年平均效率：(11.81 + 12.12) / 2 = 11.97
# 下半年行程（七月到十二月）：Aug 10 (150.0/11.0 = 13.64), Sep 25 (180.0/12.5 = 14.40)
# 下半年平均效率：(13.64 + 14.40) / 2 = 14.02
# 效率提升：14.02 - 11.97 = 2.05
# Bob Smith (driver_id = 2):
# 上半年行程：Jan 10 (100.0/9.0 = 11.11), Apr 15 (250.0/22.0 = 11.36)
# 上半年平均效率：(11.11 + 11.36) / 2 = 11.24
# 下半年行程：Oct 5 (200.0/15.0 = 13.33)
# 下半年平均效率：13.33
# 效率提升：13.33 - 11.24 = 2.10（舍入到 2 位小数）
# 未包含的司机：
# Carol Davis (driver_id = 3)：只有上半年的行程（三月，五月）
# David Wilson (driver_id = 4)：只有下半年的行程（七月，十一月）
# Emma Brown (driver_id = 5)：只有上半年的行程（二月）
# 输出表按提升效率降序排列，然后按司机名字升序排列。

import pandas as pd

# def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
#
#
# data = [[1, 201, '2024-03-01 10:00:00', 'app_open', 'S001', None], [2, 201, '2024-03-01 10:05:00', 'scroll', 'S001', 500], [3, 201, '2024-03-01 10:10:00', 'scroll', 'S001', 750], [4, 201, '2024-03-01 10:15:00', 'scroll', 'S001', 600], [5, 201, '2024-03-01 10:20:00', 'scroll', 'S001', 800], [6, 201, '2024-03-01 10:25:00', 'scroll', 'S001', 550], [7, 201, '2024-03-01 10:30:00', 'scroll', 'S001', 900], [8, 201, '2024-03-01 10:35:00', 'app_close', 'S001', None], [9, 202, '2024-03-01 11:00:00', 'app_open', 'S002', None], [10, 202, '2024-03-01 11:02:00', 'click', 'S002', None], [11, 202, '2024-03-01 11:05:00', 'scroll', 'S002', 400], [12, 202, '2024-03-01 11:08:00', 'click', 'S002', None], [13, 202, '2024-03-01 11:10:00', 'scroll', 'S002', 350], [14, 202, '2024-03-01 11:15:00', 'purchase', 'S002', 50], [15, 202, '2024-03-01 11:20:00', 'app_close', 'S002', None], [16, 203, '2024-03-01 12:00:00', 'app_open', 'S003', None], [17, 203, '2024-03-01 12:10:00', 'scroll', 'S003', 1000], [18, 203, '2024-03-01 12:20:00', 'scroll', 'S003', 1200], [19, 203, '2024-03-01 12:25:00', 'click', 'S003', None], [20, 203, '2024-03-01 12:30:00', 'scroll', 'S003', 800], [21, 203, '2024-03-01 12:40:00', 'scroll', 'S003', 900], [22, 203, '2024-03-01 12:50:00', 'scroll', 'S003', 1100], [23, 203, '2024-03-01 13:00:00', 'app_close', 'S003', None], [24, 204, '2024-03-01 14:00:00', 'app_open', 'S004', None], [25, 204, '2024-03-01 14:05:00', 'scroll', 'S004', 600], [26, 204, '2024-03-01 14:08:00', 'scroll', 'S004', 700], [27, 204, '2024-03-01 14:10:00', 'click', 'S004', None], [28, 204, '2024-03-01 14:12:00', 'app_close', 'S004', None]]
# app_events = pd.DataFrame(data, columns=["event_id", "user_id", "event_timestamp", "event_type", "session_id", "event_value"])
#
# print(find_zombie_sessions(app_events))


# -- Write your PostgreSQL query statement below
# select a.driver_id, b.driver_name, first_half_avg, second_half_avg, efficiency_improvement from (
# select driver_id, round(first_half_avg, 2) first_half_avg,
#         round(second_half_avg, 2) second_half_avg,
#         round(second_half_avg - first_half_avg, 2) efficiency_improvement from
# (select driver_id,
# avg(case when EXTRACT(MONTH FROM trip_date) between 1 and 6 then distance_km / fuel_consumed end) first_half_avg,
# avg(case when EXTRACT(MONTH FROM trip_date) between 7 and 12 then distance_km / fuel_consumed end) second_half_avg
# from trips group by driver_id )
# where first_half_avg is not null and second_half_avg is not null and first_half_avg < second_half_avg) a
# left join drivers b on a.driver_id=b.driver_id
# order by efficiency_improvement desc, driver_name
# ;


