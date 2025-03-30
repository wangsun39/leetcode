# 表： Employee
#
# +--------------+---------+
# | 列名          | 类型    |
# +--------------+---------+
# | id           | int     |
# | name         | varchar |
# | salary       | int     |
# | departmentId | int     |
# +--------------+---------+
# 在 SQL 中，id是此表的主键。
# departmentId 是 Department 表中 id 的外键（在 Pandas 中称为 join key）。
# 此表的每一行都表示员工的 id、姓名和工资。它还包含他们所在部门的 id。
#
#
# 表： Department
#
# +-------------+---------+
# | 列名         | 类型    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# 在 SQL 中，id 是此表的主键列。
# 此表的每一行都表示一个部门的 id 及其名称。
#
#
# 查找出每个部门中薪资最高的员工。
# 按 任意顺序 返回结果表。
# 查询结果格式如下例所示。
#
#
#
# 示例 1:
#
# 输入：
# Employee 表:
# +----+-------+--------+--------------+
# | id | name  | salary | departmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Jim   | 90000  | 1            |
# | 3  | Henry | 80000  | 2            |
# | 4  | Sam   | 60000  | 2            |
# | 5  | Max   | 90000  | 1            |
# +----+-------+--------+--------------+
# Department 表:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | IT    |
# | 2  | Sales |
# +----+-------+
# 输出：
# +------------+----------+--------+
# | Department | Employee | Salary |
# +------------+----------+--------+
# | IT         | Jim      | 90000  |
# | Sales      | Henry    | 80000  |
# | IT         | Max      | 90000  |
# +------------+----------+--------+
# 解释：Max 和 Jim 在 IT 部门的工资都是最高的，Henry 在销售部的工资最高。

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    grouped = employee.groupby('departmentId')
    # print(grouped)
    mx_salary = grouped['salary'].max().reset_index()
    # print(mx_salary)
    df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    # print(df)
    df = pd.merge(mx_salary, df, left_on='departmentId', right_on='departmentId', how='left')
    ans = df[df['salary_x'] == df['salary_y']][['name_y', 'name_x', 'salary_x']]
    ans.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary_x': 'Salary'}, inplace=True)
    # print(ans)

    return ans



data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})



print(department_highest_salary(employee, department))

# Write your MySQL query statement below
# SELECT d.name Department,
#          e.name Employee,
#          a.mx Salary
# FROM
#     (SELECT departmentId,
#          max(salary) mx
#     FROM Employee
#     GROUP BY  departmentId) a, Employee e, Department d
# WHERE e.departmentId = a.departmentId
#         AND mx=e.salary
#         AND a.departmentId=d.id;
