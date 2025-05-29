# 表: Triangle
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# 在 SQL 中，(x, y, z)是该表的主键列。
# 该表的每一行包含三个线段的长度。
#
#
# 对每三个线段报告它们是否可以形成一个三角形。
#
# 以 任意顺序 返回结果表。
#
# 查询结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入:
# Triangle 表:
# +----+----+----+
# | x  | y  | z  |
# +----+----+----+
# | 13 | 15 | 30 |
# | 10 | 20 | 15 |
# +----+----+----+
# 输出:
# +----+----+----+----------+
# | x  | y  | z  | triangle |
# +----+----+----+----------+
# | 13 | 15 | 30 | No       |
# | 10 | 20 | 15 | Yes      |
# +----+----+----+----------+

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    ans = triangle.copy()
    ans['triangle'] = 'No'
    # print(ans[(ans['x'] + ans['y'] > ans['z']) & (ans['x'] + ans['z'] > ans['y']) & (ans['y'] + ans['z'] > ans['x'])])
    ans['triangle'] = 'No'
    ans.loc[(ans['x'] + ans['y'] > ans['z']) & (ans['x'] + ans['z'] > ans['y']) & (ans['y'] + ans['z'] > ans['x']), 'triangle'] = 'Yes'
    return ans



data = [[13, 15, 30], [10, 20, 15]]
triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x':'Int64', 'y':'Int64', 'z':'Int64'})


print(triangle_judgement(triangle))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select x,y,z,
#     case when x + y > z and x + z > y and y + z > x then 'Yes'
#     else 'No' end triangle
# from Triangle;


