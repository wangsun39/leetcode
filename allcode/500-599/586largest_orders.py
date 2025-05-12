# 表: Orders
#
# +-----------------+----------+
# | Column Name     | Type     |
# +-----------------+----------+
# | order_number    | int      |
# | customer_number | int      |
# +-----------------+----------+
# 在 SQL 中，Order_number是该表的主键。
# 此表包含关于订单ID和客户ID的信息。
#
#
# 查找下了 最多订单 的客户的 customer_number 。
#
# 测试用例生成后， 恰好有一个客户 比任何其他客户下了更多的订单。
#
# 查询结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入:
# Orders 表:
# +--------------+-----------------+
# | order_number | customer_number |
# +--------------+-----------------+
# | 1            | 1               |
# | 2            | 2               |
# | 3            | 3               |
# | 4            | 3               |
# +--------------+-----------------+
# 输出:
# +-----------------+
# | customer_number |
# +-----------------+
# | 3               |
# +-----------------+
# 解释:
# customer_number 为 '3' 的顾客有两个订单，比顾客 '1' 或者 '2' 都要多，因为他们只有一个订单。
# 所以结果是该顾客的 customer_number ，也就是 3 。
#
#
# 进阶： 如果有多位顾客订单数并列最多，你能找到他们所有的 customer_number 吗？

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    grouped = orders.groupby(['customer_number'])
    g1 = grouped.size().reset_index(name='count')
    g1 = g1[g1['count'].max() == g1['count']]
    g1.drop("count", axis=1, inplace=True)
    print(g1)
    return g1



data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})


print(largest_orders(orders))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select customer_number from (select customer_number, count(1) as cnt from Orders group by customer_number order by cnt desc limit 1) a;

