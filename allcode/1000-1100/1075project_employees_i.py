# 项目表 Project：
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | project_id  | int     |
# | employee_id | int     |
# +-------------+---------+
# 主键为 (project_id, employee_id)。
# employee_id 是员工表 Employee 表的外键。
# 这张表的每一行表示 employee_id 的员工正在 project_id 的项目上工作。
#
#
# 员工表 Employee：
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | employee_id      | int     |
# | name             | varchar |
# | experience_years | int     |
# +------------------+---------+
# 主键是 employee_id。数据保证 experience_years 非空。
# 这张表的每一行包含一个员工的信息。
#
#
# 请写一个 SQL 语句，查询每一个项目中员工的 平均 工作年限，精确到小数点后两位。
#
# 以 任意 顺序返回结果表。
#
# 查询结果的格式如下。
#
#
#
# 示例 1:
#
# 输入：
# Project 表：
# +-------------+-------------+
# | project_id  | employee_id |
# +-------------+-------------+
# | 1           | 1           |
# | 1           | 2           |
# | 1           | 3           |
# | 2           | 1           |
# | 2           | 4           |
# +-------------+-------------+
#
# Employee 表：
# +-------------+--------+------------------+
# | employee_id | name   | experience_years |
# +-------------+--------+------------------+
# | 1           | Khaled | 3                |
# | 2           | Ali    | 2                |
# | 3           | John   | 1                |
# | 4           | Doe    | 2                |
# +-------------+--------+------------------+
#
# 输出：
# +-------------+---------------+
# | project_id  | average_years |
# +-------------+---------------+
# | 1           | 2.00          |
# | 2           | 2.50          |
# +-------------+---------------+
# 解释：第一个项目中，员工的平均工作年限是 (3 + 2 + 1) / 3 = 2.00；第二个项目中，员工的平均工作年限是 (3 + 2) / 2 = 2.50

import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    mg = pd.merge(project, employee, left_on='employee_id', right_on='employee_id', how='inner')
    grouped = mg.groupby('project_id')
    ans = grouped.agg({'experience_years': 'sum', 'project_id': 'count'}).rename(columns={'experience_years': 's', 'project_id': 'count'}).reset_index()
    ans['average_years'] = round(ans['s'] / ans['count'], 2)
    return ans[['project_id', 'average_years']]


data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype({'project_id':'Int64', 'employee_id':'Int64'})
data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype({'employee_id':'Int64', 'name':'object', 'experience_years':'Int64'})


print(project_employees_i(project, employee))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL




