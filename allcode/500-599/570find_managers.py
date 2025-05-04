# 表: Employee
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | department  | varchar |
# | managerId   | int     |
# +-------------+---------+
# id 是此表的主键（具有唯一值的列）。
# 该表的每一行表示雇员的名字、他们的部门和他们的经理的id。
# 如果managerId为空，则该员工没有经理。
# 没有员工会成为自己的管理者。
#
#
# 编写一个解决方案，找出至少有五个直接下属的经理。
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
# Employee 表:
# +-----+-------+------------+-----------+
# | id  | name  | department | managerId |
# +-----+-------+------------+-----------+
# | 101 | John  | A          | Null      |
# | 102 | Dan   | A          | 101       |
# | 103 | James | A          | 101       |
# | 104 | Amy   | A          | 101       |
# | 105 | Anne  | A          | 101       |
# | 106 | Ron   | B          | 101       |
# +-----+-------+------------+-----------+
# 输出:
# +------+
# | name |
# +------+
# | John |
# +------+

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    selected = employee[employee['managerId'] != None]
    grouped = selected.groupby('managerId')
    g1 = grouped.size().reset_index(name='count')
    print(g1)
    print(g1.to_markdown(index=False))
    g1 = g1[g1['count']>=5]
    g2 = pd.merge(employee, g1, left_on='id', right_on='managerId', how='inner')
    # print()
    return g2[['name']]


data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101], [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})


print(find_managers(employee))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select a.name from employee a,
# (select managerId, count(*) as cnt from employee where managerId is not null
# group by managerId having count(*)>=5) b where a.id=b.managerId;

