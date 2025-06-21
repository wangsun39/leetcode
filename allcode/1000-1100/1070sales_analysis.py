# 销售表 Sales：
#
# +-------------+-------+
# | Column Name | Type  |
# +-------------+-------+
# | sale_id     | int   |
# | product_id  | int   |
# | year        | int   |
# | quantity    | int   |
# | price       | int   |
# +-------------+-------+
# (sale_id, year) 是这张表的主键（具有唯一值的列的组合）。
# product_id 是产品表的外键（reference 列）。
# 这张表的每一行都表示：编号 product_id 的产品在某一年的销售额。
# 一个产品可能在同一年内有多个销售条目。
# 请注意，价格是按每单位计的。
# 编写解决方案，选出每个售出过的产品 第一年 销售的 产品 id、年份、数量 和 价格。
#
# 对每个 product_id，找到其在Sales表中首次出现的最早年份。
# 返回该产品在该年度的 所有 销售条目。
# 返回一张有这些列的表：product_id，first_year，quantity 和 price。
#
# 结果表中的条目可以按 任意顺序 排列。
#
#
#
# 示例 1：
#
# 输入：
# Sales 表：
# +---------+------------+------+----------+-------+
# | sale_id | product_id | year | quantity | price |
# +---------+------------+------+----------+-------+
# | 1       | 100        | 2008 | 10       | 5000  |
# | 2       | 100        | 2009 | 12       | 5000  |
# | 7       | 200        | 2011 | 15       | 9000  |
# +---------+------------+------+----------+-------+
# 输出：
# +------------+------------+----------+-------+
# | product_id | first_year | quantity | price |
# +------------+------------+----------+-------+
# | 100        | 2008       | 10       | 5000  |
# | 200        | 2011       | 15       | 9000  |
# +------------+------------+----------+-------+

import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    print(sales.to_markdown(index=False))
    sales['first_year'] = sales.groupby('product_id')['year'].transform('min')
    # print(sales)
    ans = sales[sales['year'] == sales['first_year']][['product_id', 'first_year', 'quantity', 'price']]

    print(ans.to_markdown(index=False))
    return ans


data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})


print(sales_analysis(sales))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select a.product_id , b.first_year , a.quantity , a.price from Sales a,
# (select product_id, min(year) first_year from Sales group by product_id) b
# where a.product_id=b.product_id and a.year=b.first_year;


