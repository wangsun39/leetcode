# Employees 表：
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | name          | varchar |
# +---------------+---------+
# 在 SQL 中，id 是这张表的主键。
# 这张表的每一行分别代表了某公司其中一位员工的名字和 ID 。
#
#
# EmployeeUNI 表：
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | unique_id     | int     |
# +---------------+---------+
# 在 SQL 中，(id, unique_id) 是这张表的主键。
# 这张表的每一行包含了该公司某位员工的 ID 和他的唯一标识码（unique ID）。
#
#
# 展示每位用户的 唯一标识码（unique ID ）；如果某位员工没有唯一标识码，使用 null 填充即可。
#
# 你可以以 任意 顺序返回结果表。
#
# 返回结果的格式如下例所示。
#
#
#
# 示例 1：
#
# 输入：
# Employees 表:
# +----+----------+
# | id | name     |
# +----+----------+
# | 1  | Alice    |
# | 7  | Bob      |
# | 11 | Meir     |
# | 90 | Winston  |
# | 3  | Jonathan |
# +----+----------+
# EmployeeUNI 表:
# +----+-----------+
# | id | unique_id |
# +----+-----------+
# | 3  | 1         |
# | 11 | 2         |
# | 90 | 3         |
# +----+-----------+
# 输出：
# +-----------+----------+
# | unique_id | name     |
# +-----------+----------+
# | null      | Alice    |
# | null      | Bob      |
# | 2         | Meir     |
# | 3         | Winston  |
# | 1         | Jonathan |
# +-----------+----------+
# 解释：
# Alice and Bob 没有唯一标识码, 因此我们使用 null 替代。
# Meir 的唯一标识码是 2 。
# Winston 的唯一标识码是 3 。
# Jonathan 唯一标识码是 1 。

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    mg = pd.merge(employees, employee_uni, left_on='id', right_on='id', how='left')
    return mg[['unique_id', 'name']]


data = [[1, 'Alice'], [7, 'Bob'], [11, 'Meir'], [90, 'Winston'], [3, 'Jonathan']]
employees = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'int64', 'name':'object'})
data = [[3, 1], [11, 2], [90, 3]]
employee_uni = pd.DataFrame(data, columns=['id', 'unique_id']).astype({'id':'int64', 'unique_id':'int64'})


print(replace_employee_id(employees, employee_uni))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select b.unique_id, a.name from Employees a left join EmployeeUNI b on a.id=b.id;




