# 表： Users
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | join_date      | date    |
# | favorite_brand | varchar |
# +----------------+---------+
# user_id 是此表主键（具有唯一值的列）。
# 表中描述了购物网站的用户信息，用户可以在此网站上进行商品买卖。
#
#
# 表： Orders
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | order_id      | int     |
# | order_date    | date    |
# | item_id       | int     |
# | buyer_id      | int     |
# | seller_id     | int     |
# +---------------+---------+
# order_id 是此表主键（具有唯一值的列）。
# item_id 是 Items 表的外键（reference 列）。
# （buyer_id，seller_id）是 User 表的外键。
#
#
# 表：Items
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | item_id       | int     |
# | item_brand    | varchar |
# +---------------+---------+
# item_id 是此表的主键（具有唯一值的列）。
#
#
# 编写解决方案找出每个用户的注册日期和在 2019 年作为买家的订单总数。
#
# 以 任意顺序 返回结果表。
#
# 查询结果格式如下。
#
#
#
# 示例 1:
#
# 输入：
# Users 表:
# +---------+------------+----------------+
# | user_id | join_date  | favorite_brand |
# +---------+------------+----------------+
# | 1       | 2018-01-01 | Lenovo         |
# | 2       | 2018-02-09 | Samsung        |
# | 3       | 2018-01-19 | LG             |
# | 4       | 2018-05-21 | HP             |
# +---------+------------+----------------+
# Orders 表:
# +----------+------------+---------+----------+-----------+
# | order_id | order_date | item_id | buyer_id | seller_id |
# +----------+------------+---------+----------+-----------+
# | 1        | 2019-08-01 | 4       | 1        | 2         |
# | 2        | 2018-08-02 | 2       | 1        | 3         |
# | 3        | 2019-08-03 | 3       | 2        | 3         |
# | 4        | 2018-08-04 | 1       | 4        | 2         |
# | 5        | 2018-08-04 | 1       | 3        | 4         |
# | 6        | 2019-08-05 | 2       | 2        | 4         |
# +----------+------------+---------+----------+-----------+
# Items 表:
# +---------+------------+
# | item_id | item_brand |
# +---------+------------+
# | 1       | Samsung    |
# | 2       | Lenovo     |
# | 3       | LG         |
# | 4       | HP         |
# +---------+------------+
# 输出：
# +-----------+------------+----------------+
# | buyer_id  | join_date  | orders_in_2019 |
# +-----------+------------+----------------+
# | 1         | 2018-01-01 | 1              |
# | 2         | 2018-02-09 | 2              |
# | 3         | 2018-01-19 | 0              |
# | 4         | 2018-05-21 | 0              |
# +-----------+------------+----------------+

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders2019 = orders[(orders['order_date']>='2019-01-01')&(orders['order_date']<'2020-01-01')]
    grouped = orders2019.groupby('buyer_id')
    g = grouped.size().reset_index(name='count')
    # print(g)
    ans = pd.merge(users, g, left_on='user_id', right_on='buyer_id', how='left')
    ans = ans[['user_id', 'join_date', 'count']]
    ans['count'] = ans['count'].fillna(0)
    ans.rename(columns={'user_id': 'buyer_id', 'count': 'orders_in_2019'}, inplace=True)
    return ans




data = [[1, '2018-01-01', 'Lenovo'], [2, '2018-02-09', 'Samsung'], [3, '2018-01-19', 'LG'], [4, '2018-05-21', 'HP']]
users = pd.DataFrame(data, columns=['user_id', 'join_date', 'favorite_brand']).astype({'user_id':'Int64', 'join_date':'datetime64[ns]', 'favorite_brand':'object'})
data = [[1, '2019-08-01', 4, 1, 2], [2, '2018-08-02', 2, 1, 3], [3, '2019-08-03', 3, 2, 3], [4, '2018-08-04', 1, 4, 2], [5, '2018-08-04', 1, 3, 4], [6, '2019-08-05', 2, 2, 4]]
orders = pd.DataFrame(data, columns=['order_id', 'order_date', 'item_id', 'buyer_id', 'seller_id']).astype({'order_id':'Int64', 'order_date':'datetime64[ns]', 'item_id':'Int64', 'buyer_id':'Int64', 'seller_id':'Int64'})
data = [[1, 'Samsung'], [2, 'Lenovo'], [3, 'LG'], [4, 'HP']]
items = pd.DataFrame(data, columns=['item_id', 'item_brand']).astype({'item_id':'Int64', 'item_brand':'object'})


print(market_analysis(users, orders, items))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select user_id buyer_id, join_date, COALESCE(b.orders_in_2019, 0) orders_in_2019 from Users a left join
# (select buyer_id, count(1) orders_in_2019 from Orders where order_date between DATE '2019-01-01' and DATE '2020-01-01' group by buyer_id) b
# on a.user_id=b.buyer_id;



