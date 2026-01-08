# 表: Employees
#
# +-------------+---------+
# | 列名        | 类型     |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id 是这个表的主键(具有唯一值的列)。
# 此表的每一行给出了雇员id ，名字和薪水。
#
#
# 编写解决方案，计算每个雇员的奖金。如果一个雇员的 id 是 奇数 并且他的名字不是以 'M' 开头，那么他的奖金是他工资的 100% ，否则奖金为 0 。
#
# 返回的结果按照 employee_id 排序。
#
# 返回结果格式如下面的例子所示。
#
#
#
# 示例 1:
#
# 输入：
# Employees 表:
# +-------------+---------+--------+
# | employee_id | name    | salary |
# +-------------+---------+--------+
# | 2           | Meir    | 3000   |
# | 3           | Michael | 3800   |
# | 7           | Addilyn | 7400   |
# | 8           | Juan    | 6100   |
# | 9           | Kannon  | 7700   |
# +-------------+---------+--------+
# 输出：
# +-------------+-------+
# | employee_id | bonus |
# +-------------+-------+
# | 2           | 0     |
# | 3           | 0     |
# | 7           | 7400  |
# | 8           | 0     |
# | 9           | 7700  |
# +-------------+-------+
# 解释：
# 因为雇员id是偶数，所以雇员id 是2和8的两个雇员得到的奖金是0。
# 雇员id为3的因为他的名字以'M'开头，所以，奖金是0。
# 其他的雇员得到了百分之百的奖金。

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    ans = employees.assign(bonus=0)
    ans.loc[(ans['employee_id'] & 1) & (ans['name'].str[0] != 'M'), 'bonus'] = ans['salary']
    ans.sort_values(by='employee_id', inplace=True)
    return ans[['employee_id', 'bonus']]


data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})


print(calculate_special_bonus(employees))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select employee_id,
# case when employee_id & 1 = 1 and substring(name,1,1) != 'M' then salary
# else 0 end bonus from Employees order by employee_id;



