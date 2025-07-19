# 产品数据表: Products
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | product_id    | int     |
# | new_price     | int     |
# | change_date   | date    |
# +---------------+---------+
# (product_id, change_date) 是此表的主键（具有唯一值的列组合）。
# 这张表的每一行分别记录了 某产品 在某个日期 更改后 的新价格。
# 一开始，所有产品价格都为 10。
#
# 编写一个解决方案，找出在 2019-08-16 所有产品的价格。
#
# 以 任意顺序 返回结果表。
#
# 结果格式如下例所示。
#
#
#
# 示例 1:
#
# 输入：
# Products 表:
# +------------+-----------+-------------+
# | product_id | new_price | change_date |
# +------------+-----------+-------------+
# | 1          | 20        | 2019-08-14  |
# | 2          | 50        | 2019-08-14  |
# | 1          | 30        | 2019-08-15  |
# | 1          | 35        | 2019-08-16  |
# | 2          | 65        | 2019-08-17  |
# | 3          | 20        | 2019-08-18  |
# +------------+-----------+-------------+
# 输出：
# +------------+-------+
# | product_id | price |
# +------------+-------+
# | 2          | 50    |
# | 1          | 35    |
# | 3          | 10    |
# +------------+-------+

import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    p1 = products.drop_duplicates(subset=['product_id'], keep='first')
    p1 = p1[['product_id']]
    p2 = products[products['change_date'] <= '2019-08-16']
    grouped = p2.groupby(['product_id'])
    grouped = grouped['change_date'].max().reset_index()
    p3 = pd.merge(p2, grouped, left_on=['product_id', 'change_date'], right_on=['product_id', 'change_date'], how='inner')
    # print(p3)
    ans = pd.merge(p1, p3, left_on=['product_id'], right_on=['product_id'], how='left')[['product_id', 'new_price']]
    ans.rename(columns={'new_price': 'price'}, inplace=True)
    ans['price'] = ans['price'].fillna(10)
    return ans




data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'], [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype({'product_id':'Int64', 'new_price':'Int64', 'change_date':'datetime64[ns]'})


print(price_at_given_date(products))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select a.product_id, COALESCE(b.new_price, 10) price from (select distinct product_id product_id from Products) a left join
# (select product_id, new_price from Products where (product_id, change_date) in
# (select product_id, max(change_date) dat from Products where change_date<='2019-08-16' group by product_id)) b
# on a.product_id=b.product_id;



