# 表：Employee
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | empId       | int     |
# | name        | varchar |
# | supervisor  | int     |
# | salary      | int     |
# +-------------+---------+
# empId 是该表中具有唯一值的列。
# 该表的每一行都表示员工的姓名和 id，以及他们的工资和经理的 id。
#
#
# 表：Bonus
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | empId       | int  |
# | bonus       | int  |
# +-------------+------+
# empId 是该表具有唯一值的列。
# empId 是 Employee 表中 empId 的外键(reference 列)。
# 该表的每一行都包含一个员工的 id 和他们各自的奖金。
#
#
# 编写解决方案，报告每个奖金 少于 1000 的员工的姓名和奖金数额。
#
# 以 任意顺序 返回结果表。
#
# 结果格式如下所示。
#
#
#
# 示例 1：
#
# 输入：
# Employee table:
# +-------+--------+------------+--------+
# | empId | name   | supervisor | salary |
# +-------+--------+------------+--------+
# | 3     | Brad   | null       | 4000   |
# | 1     | John   | 3          | 1000   |
# | 2     | Dan    | 3          | 2000   |
# | 4     | Thomas | 3          | 4000   |
# +-------+--------+------------+--------+
# Bonus table:
# +-------+-------+
# | empId | bonus |
# +-------+-------+
# | 2     | 500   |
# | 4     | 2000  |
# +-------+-------+
# 输出：
# +------+-------+
# | name | bonus |
# +------+-------+
# | Brad | null  |
# | John | null  |
# | Dan  | 500   |
# +------+-------+

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:

    mg = pd.merge(employee, bonus, left_on='empId', right_on='empId', how='left')
    mg = mg[(mg['bonus']<1000) | (mg['bonus'].isna())]
    print(mg)
    return mg[['name', 'bonus']]


data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype({'empId':'Int64', 'name':'object', 'supervisor':'Int64', 'salary':'Int64'})
data = [[2, 500], [4, 2000]]
bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId':'Int64', 'bonus':'Int64'})


print(employee_bonus(employee, bonus))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select employee.name, bonus.bonus from employee left join bonus
# on employee.empId=bonus.empId where (bonus.bonus<1000 or bonus.bonus is null);

