# 表: Activity
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | machine_id     | int     |
# | process_id     | int     |
# | activity_type  | enum    |
# | timestamp      | float   |
# +----------------+---------+
# 该表展示了一家工厂网站的用户活动。
# (machine_id, process_id, activity_type) 是当前表的主键（具有唯一值的列的组合）。
# machine_id 是一台机器的ID号。
# process_id 是运行在各机器上的进程ID号。
# activity_type 是枚举类型 ('start', 'end')。
# timestamp 是浮点类型,代表当前时间(以秒为单位)。
# 'start' 代表该进程在这台机器上的开始运行时间戳 , 'end' 代表该进程在这台机器上的终止运行时间戳。
# 同一台机器，同一个进程都有一对开始时间戳和结束时间戳，而且开始时间戳永远在结束时间戳前面。
#
#
# 现在有一个工厂网站由几台机器运行，每台机器上运行着 相同数量的进程 。编写解决方案，计算每台机器各自完成一个进程任务的平均耗时。
#
# 完成一个进程任务的时间指进程的'end' 时间戳 减去 'start' 时间戳。平均耗时通过计算每台机器上所有进程任务的总耗费时间除以机器上的总进程数量获得。
#
# 结果表必须包含machine_id（机器ID） 和对应的 average time（平均耗时） 别名 processing_time，且四舍五入保留3位小数。
#
# 以 任意顺序 返回表。
#
# 具体参考例子如下。
#
#
#
# 示例 1:
#
# 输入：
# Activity table:
# +------------+------------+---------------+-----------+
# | machine_id | process_id | activity_type | timestamp |
# +------------+------------+---------------+-----------+
# | 0          | 0          | start         | 0.712     |
# | 0          | 0          | end           | 1.520     |
# | 0          | 1          | start         | 3.140     |
# | 0          | 1          | end           | 4.120     |
# | 1          | 0          | start         | 0.550     |
# | 1          | 0          | end           | 1.550     |
# | 1          | 1          | start         | 0.430     |
# | 1          | 1          | end           | 1.420     |
# | 2          | 0          | start         | 4.100     |
# | 2          | 0          | end           | 4.512     |
# | 2          | 1          | start         | 2.500     |
# | 2          | 1          | end           | 5.000     |
# +------------+------------+---------------+-----------+
# 输出：
# +------------+-----------------+
# | machine_id | processing_time |
# +------------+-----------------+
# | 0          | 0.894           |
# | 1          | 0.995           |
# | 2          | 1.456           |
# +------------+-----------------+
# 解释：
# 一共有3台机器,每台机器运行着两个进程.
# 机器 0 的平均耗时: ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
# 机器 1 的平均耗时: ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
# 机器 2 的平均耗时: ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    a = pd.merge(activity, activity, on=['machine_id', 'process_id'], how='inner')
    # print(a)
    a = a[(a['activity_type_x'] == 'start') & (a['activity_type_y'] == 'end')]
    a['cost'] = a['timestamp_y'] - a['timestamp_x']
    # print(a)
    ans = (
        a
        .groupby(['machine_id'], dropna=False)  # 显式保留 NaN
        .agg(
            cnt=('activity_type_x', 'size'),  # 新增：统计每组的行数
            cost=('cost', 'sum')
        )
    ).reset_index()
    ans['processing_time'] = round(ans['cost'] / ans['cnt'], 3)
    ans.drop(columns=['cnt', 'cost'], inplace=True)
    return ans



data = [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12], [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42], [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]]
activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})


print(get_average_time(activity))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select a.machine_id, round((sum(b.timestamp - a.timestamp)/count(1))::NUMERIC, 3) as processing_time from Activity a, Activity b
# where a.machine_id=b.machine_id and a.process_id=b.process_id and a.activity_type!=b.activity_type and a.activity_type='start'
# group by a.machine_id;




