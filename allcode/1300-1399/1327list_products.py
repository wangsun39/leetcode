# 表: Products
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | product_id       | int     |
# | product_name     | varchar |
# | product_category | varchar |
# +------------------+---------+
# product_id 是该表主键(具有唯一值的列)。
# 该表包含该公司产品的数据。
#
#
# 表: Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | order_date    | date    |
# | unit          | int     |
# +---------------+---------+
# 该表可能包含重复行。
# product_id 是表单 Products 的外键（reference 列）。
# unit 是在日期 order_date 内下单产品的数目。
#
#
# 写一个解决方案，要求获取在 2020 年 2 月份下单的数量不少于 100 的产品的名字和数目。
#
# 返回结果表单的 顺序无要求 。
#
# 查询结果的格式如下。
#
#
#
# 示例 1:
#
# 输入：
# Products 表:
# +-------------+-----------------------+------------------+
# | product_id  | product_name          | product_category |
# +-------------+-----------------------+------------------+
# | 1           | Leetcode Solutions    | Book             |
# | 2           | Jewels of Stringology | Book             |
# | 3           | HP                    | Laptop           |
# | 4           | Lenovo                | Laptop           |
# | 5           | Leetcode Kit          | T-shirt          |
# +-------------+-----------------------+------------------+
# Orders 表:
# +--------------+--------------+----------+
# | product_id   | order_date   | unit     |
# +--------------+--------------+----------+
# | 1            | 2020-02-05   | 60       |
# | 1            | 2020-02-10   | 70       |
# | 2            | 2020-01-18   | 30       |
# | 2            | 2020-02-11   | 80       |
# | 3            | 2020-02-17   | 2        |
# | 3            | 2020-02-24   | 3        |
# | 4            | 2020-03-01   | 20       |
# | 4            | 2020-03-04   | 30       |
# | 4            | 2020-03-04   | 60       |
# | 5            | 2020-02-25   | 50       |
# | 5            | 2020-02-27   | 50       |
# | 5            | 2020-03-01   | 50       |
# +--------------+--------------+----------+
# 输出：
# +--------------------+---------+
# | product_name       | unit    |
# +--------------------+---------+
# | Leetcode Solutions | 130     |
# | Leetcode Kit       | 100     |
# +--------------------+---------+
# 解释：
# 2020 年 2 月份下单 product_id = 1 的产品的数目总和为 (60 + 70) = 130 。
# 2020 年 2 月份下单 product_id = 2 的产品的数目总和为 80 。
# 2020 年 2 月份下单 product_id = 3 的产品的数目总和为 (2 + 3) = 5 。
# 2020 年 2 月份 product_id = 4 的产品并没有下单。
# 2020 年 2 月份下单 product_id = 5 的产品的数目总和为 (50 + 50) = 100 。


import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date'] >= '2020-02-01') & (orders['order_date'] < '2020-03-01')]
    ans = pd.merge(products, orders, left_on='product_id', right_on='product_id', how='inner')
    print(ans)
    ans = (
        ans
        .groupby(['product_name'], dropna=False)  # 显式保留 NaN
        .agg(
            unit=('unit', 'sum')
        )
    ).reset_index()
    ans = ans[ans['unit'] >= 100]
    ans.drop(columns=['product_id'], inplace=True)
    return ans


data = [[1, 'Leetcode Solutions', 'Book'], [2, 'Jewels of Stringology', 'Book'], [3, 'HP', 'Laptop'], [4, 'Lenovo', 'Laptop'], [5, 'Leetcode Kit', 'T-shirt']]
products = pd.DataFrame(data, columns=['product_id', 'product_name', 'product_category']).astype({'product_id':'Int64', 'product_name':'object', 'product_category':'object'})
data = [[1, '2020-02-05', 60], [1, '2020-02-10', 70], [2, '2020-01-18', 30], [2, '2020-02-11', 80], [3, '2020-02-17', 2], [3, '2020-02-24', 3], [4, '2020-03-01', 20], [4, '2020-03-04', 30], [4, '2020-03-04', 60], [5, '2020-02-25', 50], [5, '2020-02-27', 50], [5, '2020-03-01', 50]]
orders = pd.DataFrame(data, columns=['product_id', 'order_date', 'unit']).astype({'product_id':'Int64', 'order_date':'datetime64[ns]', 'unit':'Int64'})


print(list_products(products, orders))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select b.product_name, sum(a.unit) unit from orders a, products b
# where a.order_date between '2020-02-01' and '2020-02-29' and a.product_id=b.product_id group by a.product_id,b.product_name having sum(a.unit)>=100;




