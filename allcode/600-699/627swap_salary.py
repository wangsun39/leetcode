# Salary 表：
#
# +-------------+----------+
# | Column Name | Type     |
# +-------------+----------+
# | id          | int      |
# | name        | varchar  |
# | sex         | ENUM     |
# | salary      | int      |
# +-------------+----------+
# id 是这个表的主键（具有唯一值的列）。
# sex 这一列的值是 ENUM 类型，只能从 ('m', 'f') 中取。
# 本表包含公司雇员的信息。
#
#
# 请你编写一个解决方案来交换所有的 'f' 和 'm' （即，将所有 'f' 变为 'm' ，反之亦然），仅使用 单个 update 语句 ，且不产生中间临时表。
#
# 注意，你必须仅使用一条 update 语句，且 不能 使用 select 语句。
#
# 结果如下例所示。
#
#
#
# 示例 1:
#
# 输入：
# Salary 表：
# +----+------+-----+--------+
# | id | name | sex | salary |
# +----+------+-----+--------+
# | 1  | A    | m   | 2500   |
# | 2  | B    | f   | 1500   |
# | 3  | C    | m   | 5500   |
# | 4  | D    | f   | 500    |
# +----+------+-----+--------+
# 输出：
# +----+------+-----+--------+
# | id | name | sex | salary |
# +----+------+-----+--------+
# | 1  | A    | f   | 2500   |
# | 2  | B    | m   | 1500   |
# | 3  | C    | f   | 5500   |
# | 4  | D    | m   | 500    |
# +----+------+-----+--------+
# 解释：
# (1, A) 和 (3, C) 从 'm' 变为 'f' 。
# (2, B) 和 (4, D) 从 'f' 变为 'm' 。


import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary.loc[salary['sex'] == 'f', 'sex'] = 'x'
    salary.loc[salary['sex'] == 'm', 'sex'] = 'f'
    salary.loc[salary['sex'] == 'x', 'sex'] = 'm'
    return salary



data = [[1, 'A', 'm', 2500], [2, 'B', 'f', 1500], [3, 'C', 'm', 5500], [4, 'D', 'f', 500]]
salary = pd.DataFrame(data, columns=['id', 'name', 'sex', 'salary']).astype({'id':'Int64', 'name':'object', 'sex':'object', 'salary':'Int64'})



print(swap_salary(salary))

# -- Write your PostgreSQL query statement below

# PostgreSQL
# update salary set sex=(case when sex ='f' then 'm'
#     else 'f' end);



