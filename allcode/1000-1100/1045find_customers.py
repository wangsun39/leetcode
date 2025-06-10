# Customer 表：
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | customer_id | int     |
# | product_key | int     |
# +-------------+---------+
# 该表可能包含重复的行。
# customer_id 不为 NULL。
# product_key 是 Product 表的外键(reference 列)。
# Product 表：
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_key | int     |
# +-------------+---------+
# product_key 是这张表的主键（具有唯一值的列）。
#
#
# 编写解决方案，报告 Customer 表中购买了 Product 表中所有产品的客户的 id。
#
# 返回结果表 无顺序要求 。
#
# 返回结果格式如下所示。
#
#
#
# 示例 1：
#
# 输入：
# Customer 表：
# +-------------+-------------+
# | customer_id | product_key |
# +-------------+-------------+
# | 1           | 5           |
# | 2           | 6           |
# | 3           | 5           |
# | 3           | 6           |
# | 1           | 6           |
# +-------------+-------------+
# Product 表：
# +-------------+
# | product_key |
# +-------------+
# | 5           |
# | 6           |
# +-------------+
# 输出：
# +-------------+
# | customer_id |
# +-------------+
# | 1           |
# | 3           |
# +-------------+
# 解释：
# 购买了所有产品（5 和 6）的客户的 id 是 1 和 3 。

import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    unique = customer.drop_duplicates()
    grouped = unique.groupby('customer_id')
    g1 = grouped.size().reset_index(name='count')
    n = len(product)
    ans = g1[g1['count'] == n]
    ans = ans.drop(columns='count')
    # print(g1)
    return ans


data = [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]]
customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype({'customer_id':'Int64', 'product_key':'Int64'})
data = [[5], [6]]
product = pd.DataFrame(data, columns=['product_key']).astype({'product_key':'Int64'})


print(find_customers(customer, product))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select a.customer_id customer_id from (SELECT DISTINCT *
# FROM Customer) a group by a.customer_id having count(1)=(select count(1) from product);


