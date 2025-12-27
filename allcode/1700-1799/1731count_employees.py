# 表：Employees
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | employee_id | int      |
# | name        | varchar  |
# | reports_to  | int      |
# | age         | int      |
# +-------------+----------+
# employee_id 是这个表中具有不同值的列。
# 该表包含员工以及需要听取他们汇报的上级经理的 ID 的信息。 有些员工不需要向任何人汇报（reports_to 为空）。
#
#
# 对于此问题，我们将至少有一个其他员工需要向他汇报的员工，视为一个经理。
#
# 编写一个解决方案来返回需要听取汇报的所有经理的 ID、名称、直接向该经理汇报的员工人数，以及这些员工的平均年龄，其中该平均年龄需要四舍五入到最接近的整数。
#
# 返回的结果集需要按照 employee_id 进行排序。
#
# 结果的格式如下：
#
#
#
# 示例 1:
#
# 输入：
# Employees 表：
# +-------------+---------+------------+-----+
# | employee_id | name    | reports_to | age |
# +-------------+---------+------------+-----+
# | 9           | Hercy   | null       | 43  |
# | 6           | Alice   | 9          | 41  |
# | 4           | Bob     | 9          | 36  |
# | 2           | Winston | null       | 37  |
# +-------------+---------+------------+-----+
# 输出：
# +-------------+-------+---------------+-------------+
# | employee_id | name  | reports_count | average_age |
# +-------------+-------+---------------+-------------+
# | 9           | Hercy | 2             | 39          |
# +-------------+-------+---------------+-------------+
# 解释：
# Hercy 有两个需要向他汇报的员工, 他们是 Alice and Bob. 他们的平均年龄是 (41+36)/2 = 38.5, 四舍五入的结果是 39.
# 示例 2:
#
# 输入：
# Employees 表：
# +-------------+---------+------------+-----+
# | employee_id | name    | reports_to | age |
# |-------------|---------|------------|-----|
# | 1           | Michael | null       | 45  |
# | 2           | Alice   | 1          | 38  |
# | 3           | Bob     | 1          | 42  |
# | 4           | Charlie | 2          | 34  |
# | 5           | David   | 2          | 40  |
# | 6           | Eve     | 3          | 37  |
# | 7           | Frank   | null       | 50  |
# | 8           | Grace   | null       | 48  |
# +-------------+---------+------------+-----+
# 输出：
# +-------------+---------+---------------+-------------+
# | employee_id | name    | reports_count | average_age |
# | ----------- | ------- | ------------- | ----------- |
# | 1           | Michael | 2             | 40          |
# | 2           | Alice   | 2             | 37          |
# | 3           | Bob     | 1             | 37          |
# +-------------+---------+---------------+-------------+

import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    ans = (
        employees
        .groupby(['reports_to'])  # 显式保留 NaN
        .agg(
            reports_count=('name', 'size'),  # 新增：统计每组的行数
            average_age=('age', 'mean')
        )
    ).reset_index()
    ans = ans.merge(employees, left_on=['reports_to'], right_on=['employee_id'], how='inner')
    ans = ans[['employee_id', 'name', 'reports_count', 'average_age']]
    ans['average_age'] = ans['average_age'].apply(lambda x: int(x + 0.5))
    ans.sort_values(by='employee_id', inplace=True)
    return ans




data = [[9, 'Hercy', None, 43], [6, 'Alice', 9, 41], [4, 'Bob', 9, 36], [2, 'Winston', None, 37]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'reports_to', 'age']).astype({'employee_id':'Int64', 'name':'object', 'reports_to':'Int64', 'age':'Int64'})


print(count_employees(employees))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select employee_id, name, reports_count, average_age from
# (select reports_to, count(1) reports_count, round(sum(age)::NUMERIC/count(1)) average_age from Employees group by reports_to having reports_to is not null) a
# join Employees b on a.reports_to = b.employee_id order by employee_id;




