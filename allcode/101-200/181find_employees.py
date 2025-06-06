# 表：Employee
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id 是该表的主键（具有唯一值的列）。
# 该表的每一行都表示雇员的ID、姓名、工资和经理的ID。
#
#
# 编写解决方案，找出收入比经理高的员工。
#
# 以 任意顺序 返回结果表。
#
# 结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入:
# Employee 表:
# +----+-------+--------+-----------+
# | id | name  | salary | managerId |
# +----+-------+--------+-----------+
# | 1  | Joe   | 70000  | 3         |
# | 2  | Henry | 80000  | 4         |
# | 3  | Sam   | 60000  | Null      |
# | 4  | Max   | 90000  | Null      |
# +----+-------+--------+-----------+
# 输出:
# +----------+
# | Employee |
# +----------+
# | Joe      |
# +----------+
# 解释: Joe 是唯一挣得比经理多的雇员。

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, employee, left_on='managerId', right_on='id', how='inner')
    df = df[df['salary_x'] > df['salary_y']]
    df.rename(columns={'name_x': 'Employee'}, inplace=True)
    return df[['Employee']]


data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})



print(find_employees(employee))

# select a.name as Employee from Employee a, Employee b where a.managerId=b.id and a.salary>b.salary;
