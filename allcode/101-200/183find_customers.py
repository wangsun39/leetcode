# Customers 表：
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# 在 SQL 中，id 是该表的主键。
# 该表的每一行都表示客户的 ID 和名称。
# Orders 表：
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# 在 SQL 中，id 是该表的主键。
# customerId 是 Customers 表中 ID 的外键( Pandas 中的连接键)。
# 该表的每一行都表示订单的 ID 和订购该订单的客户的 ID。
#
#
# 找出所有从不点任何东西的顾客。
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
# Customers table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders table:
# +----+------------+
# | id | customerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# 输出：
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    print(df)
    df = df[df['id_y'].isna()]
    print(df)
    df.rename(columns={'name': 'Customers'}, inplace=True)
    return df[['Customers']]



data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})



print(find_customers(customers, orders))

# select a.name as Employee from Employee a, Employee b where a.managerId=b.id and a.salary>b.salary;
