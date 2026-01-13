# 表: Employees
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# +-------------+---------+
# employee_id 是该表中具有唯一值的列。
# 每一行表示雇员的 id 和他的姓名。
# 表: Salaries
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | salary      | int     |
# +-------------+---------+
# employee_id 是该表中具有唯一值的列。
# 每一行表示雇员的 id 和他的薪水。
#
#
# 编写解决方案，找到所有 丢失信息 的雇员 id。当满足下面一个条件时，就被认为是雇员的信息丢失：
#
# 雇员的 姓名 丢失了，或者
# 雇员的 薪水信息 丢失了
# 返回这些雇员的 id  employee_id ， 从小到大排序 。
#
# 查询结果格式如下面的例子所示。
#
#
#
# 示例 1：
#
# 输入：
# Employees table:
# +-------------+----------+
# | employee_id | name     |
# +-------------+----------+
# | 2           | Crew     |
# | 4           | Haven    |
# | 5           | Kristian |
# +-------------+----------+
# Salaries table:
# +-------------+--------+
# | employee_id | salary |
# +-------------+--------+
# | 5           | 76071  |
# | 1           | 22517  |
# | 4           | 63539  |
# +-------------+--------+
# 输出：
# +-------------+
# | employee_id |
# +-------------+
# | 1           |
# | 2           |
# +-------------+
# 解释：
# 雇员 1，2，4，5 都在这个公司工作。
# 1 号雇员的姓名丢失了。
# 2 号雇员的薪水信息丢失了。

import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    unoin = pd.concat([employees[['employee_id']], salaries[['employee_id']]], ignore_index=True)
    # print(unoin)

    ans = (
        unoin
        .groupby(['employee_id'], dropna=False)  # 显式保留 NaN
        .agg(
            count=('employee_id', 'size')
        )
    ).reset_index()
    ans = ans[ans['count'] == 1][['employee_id']]
    ans.sort_values(by='employee_id', inplace=True)
    return ans


data = [[2, 'Crew'], [4, 'Haven'], [5, 'Kristian']]
employees = pd.DataFrame(data, columns=['employee_id', 'name']).astype({'employee_id':'Int64', 'name':'object'})
data = [[5, 76071], [1, 22517], [4, 63539]]
salaries = pd.DataFrame(data, columns=['employee_id', 'salary']).astype({'employee_id':'Int64', 'salary':'Int64'})


print(find_employees(employees, salaries))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select employee_id from
# (select employee_id from Employees
# union all
# select employee_id from Salaries )  group by employee_id having count(1)=1 order by employee_id;



