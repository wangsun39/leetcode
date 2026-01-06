# 表：Products
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | store1      | int     |
# | store2      | int     |
# | store3      | int     |
# +-------------+---------+
# 在 SQL 中，这张表的主键是 product_id（产品Id）。
# 每行存储了这一产品在不同商店 store1, store2, store3 的价格。
# 如果这一产品在商店里没有出售，则值将为 null。
#
#
# 请你重构 Products 表，查询每个产品在不同商店的价格，使得输出的格式变为(product_id, store, price) 。如果这一产品在商店里没有出售，则不输出这一行。
#
# 输出结果表中的 顺序不作要求 。
#
# 查询输出格式请参考下面示例。
#
#
#
# 示例 1：
#
# 输入：
# Products table:
# +------------+--------+--------+--------+
# | product_id | store1 | store2 | store3 |
# +------------+--------+--------+--------+
# | 0          | 95     | 100    | 105    |
# | 1          | 70     | null   | 80     |
# +------------+--------+--------+--------+
# 输出：
# +------------+--------+-------+
# | product_id | store  | price |
# +------------+--------+-------+
# | 0          | store1 | 95    |
# | 0          | store2 | 100   |
# | 0          | store3 | 105   |
# | 1          | store1 | 70    |
# | 1          | store3 | 80    |
# +------------+--------+-------+
# 解释：
# 产品 0 在 store1、store2、store3 的价格分别为 95、100、105。
# 产品 1 在 store1、store3 的价格分别为 70、80。在 store2 无法买到。

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df1 = products.loc[products['store1'].notna(), ['product_id', 'store1']].assign(store='store1')
    df1.rename(columns={'store1': 'price'}, inplace=True)
    df2 = products.loc[products['store2'].notna(), ['product_id', 'store2']].assign(store='store2')
    df2.rename(columns={'store2': 'price'}, inplace=True)
    df3 = products.loc[products['store3'].notna(), ['product_id', 'store3']].assign(store='store3')
    df3.rename(columns={'store3': 'price'}, inplace=True)
    df = pd.concat([df1, df2, df3], ignore_index=True)
    return df


data = [[0, 95, 100, 105], [1, 70, None, 80]]
products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'Int64', 'store1':'Int64', 'store2':'Int64', 'store3':'Int64'})


print(rearrange_products_table(products))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select product_id, 'store1' store, store1 price from Products where store1 is not null
# union all
# select product_id, 'store2' store, store2 price from Products where store2 is not null
# union all
# select product_id, 'store3' store, store3 price from Products where store3 is not null;


import numpy as np

M = np.array([
    [-1, 3, 0, 0, 0, 3],
    [3, -1, 3, 0, 0, 0],
    [0, 3, -1, 3, 0, 0],
    [0, 0, 3, -1, 3, 0],
    [0, 0, 0, 3, -1, 3],
    [3, 0, 0, 0, 3, -1],
], dtype=float)
for A in range(56, 10000, 280):
    b = np.array([2026 - A, 2026, 2026, 2026, 2026, 2026], dtype=float)
    x = np.linalg.solve(M, b)
    print(A, x)


