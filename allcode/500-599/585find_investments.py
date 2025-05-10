# Insurance 表：
#
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | pid         | int   |
# | tiv_2015    | float |
# | tiv_2016    | float |
# | lat         | float |
# | lon         | float |
# +-------------+-------+
# pid 是这张表的主键(具有唯一值的列)。
# 表中的每一行都包含一条保险信息，其中：
# pid 是投保人的投保编号。
# tiv_2015 是该投保人在 2015 年的总投保金额，tiv_2016 是该投保人在 2016 年的总投保金额。
# lat 是投保人所在城市的纬度。题目数据确保 lat 不为空。
# lon 是投保人所在城市的经度。题目数据确保 lon 不为空。
#
#
# 编写解决方案报告 2016 年 (tiv_2016) 所有满足下述条件的投保人的投保金额之和：
#
# 他在 2015 年的投保额 (tiv_2015) 至少跟一个其他投保人在 2015 年的投保额相同。
# 他所在的城市必须与其他投保人都不同（也就是说 (lat, lon) 不能跟其他任何一个投保人完全相同）。
# tiv_2016 四舍五入的 两位小数 。
#
# 查询结果格式如下例所示。
#
#
#
# 示例 1：
#
# 输入：
# Insurance 表：
# +-----+----------+----------+-----+-----+
# | pid | tiv_2015 | tiv_2016 | lat | lon |
# +-----+----------+----------+-----+-----+
# | 1   | 10       | 5        | 10  | 10  |
# | 2   | 20       | 20       | 20  | 20  |
# | 3   | 10       | 30       | 20  | 20  |
# | 4   | 10       | 40       | 40  | 40  |
# +-----+----------+----------+-----+-----+
# 输出：
# +----------+
# | tiv_2016 |
# +----------+
# | 45.00    |
# +----------+
# 解释：
# 表中的第一条记录和最后一条记录都满足两个条件。
# tiv_2015 值为 10 与第三条和第四条记录相同，且其位置是唯一的。
#
# 第二条记录不符合任何一个条件。其 tiv_2015 与其他投保人不同，并且位置与第三条记录相同，这也导致了第三条记录不符合题目要求。
# 因此，结果是第一条记录和最后一条记录的 tiv_2016 之和，即 45 。

import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    grouped = insurance.groupby(['lat', 'lon'])
    g1 = grouped.size().reset_index(name='count')
    g1 = g1[g1['count'] == 1]
    # print(g1)
    grouped = insurance.groupby('tiv_2015')
    g2 = grouped.size().reset_index(name='count')
    g2 = g2[g2['count'] > 1]
    # print(g2)

    # ans = pd.merge(insurance, g1, on=['lat', 'lon'], how='inner')
    ans = insurance.merge(g1, on=['lat', 'lon'], how='inner')
    ans = ans.merge(g2, on=['tiv_2015'], how='inner')
    # print(round(ans['tiv_2016'].sum(), 2))
    return pd.DataFrame({"tiv_2016": [round(ans['tiv_2016'].sum(), 2)]})



data = [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]
insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype({'pid':'Int64', 'tiv_2015':'Float64', 'tiv_2016':'Float64', 'lat':'Float64', 'lon':'Float64'})


print(find_investments(insurance))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select round(sum(tiv_2016)::NUMERIC,2) as tiv_2016 from (select * from Insurance where tiv_2015 in (select tiv_2015 from Insurance group by tiv_2015 having count(1) > 1)) a,
# (select lat, lon from Insurance group by lat, lon having count(1) = 1) b
# where a.lat=b.lat and a.lon=b.lon;

