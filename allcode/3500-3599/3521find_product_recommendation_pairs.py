# 表：ProductPurchases
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | user_id     | int  |
# | product_id  | int  |
# | quantity    | int  |
# +-------------+------+
# (user_id, product_id) 是这张表的唯一主键。
# 每一行代表用户以特定数量购买的产品。
# 表：ProductInfo
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_id  | int     |
# | category    | varchar |
# | price       | decimal |
# +-------------+---------+
# product_id 是这张表的唯一主键。
# 每一行表示一个产品的类别和价格。
# 亚马逊希望根据 共同购买模式 实现 “购买此商品的用户还购买了...” 功能。编写一个解决方案以实现：
#
# 识别 被同一客户一起频繁购买的 不同 产品对（其中 product1_id < product2_id）
# 对于 每个产品对，确定有多少客户购买了这两种产品
# 如果 至少有 3 位不同的 客户同时购买了这两种产品，则认为该 产品对 适合推荐。
#
# 返回结果表以 customer_count  降序 排序，并且为了避免排序持平，以 product1_id 升序 排序，并以 product2_id 升序 排序。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# ProductPurchases 表：
#
# +---------+------------+----------+
# | user_id | product_id | quantity |
# +---------+------------+----------+
# | 1       | 101        | 2        |
# | 1       | 102        | 1        |
# | 1       | 103        | 3        |
# | 2       | 101        | 1        |
# | 2       | 102        | 5        |
# | 2       | 104        | 1        |
# | 3       | 101        | 2        |
# | 3       | 103        | 1        |
# | 3       | 105        | 4        |
# | 4       | 101        | 1        |
# | 4       | 102        | 1        |
# | 4       | 103        | 2        |
# | 4       | 104        | 3        |
# | 5       | 102        | 2        |
# | 5       | 104        | 1        |
# +---------+------------+----------+
# ProductInfo 表：
#
# +------------+-------------+-------+
# | product_id | category    | price |
# +------------+-------------+-------+
# | 101        | Electronics | 100   |
# | 102        | Books       | 20    |
# | 103        | Clothing    | 35    |
# | 104        | Kitchen     | 50    |
# | 105        | Sports      | 75    |
# +------------+-------------+-------+
# 输出：
#
# +-------------+-------------+-------------------+-------------------+----------------+
# | product1_id | product2_id | product1_category | product2_category | customer_count |
# +-------------+-------------+-------------------+-------------------+----------------+
# | 101         | 102         | Electronics       | Books             | 3              |
# | 101         | 103         | Electronics       | Clothing          | 3              |
# | 102         | 104         | Books             | Kitchen           | 3              |
# +-------------+-------------+-------------------+-------------------+----------------+
# 解释：
#
# 产品对 (101, 102)：
# 被用户 1，2 和 4 购买（3 个消费者）
# 产品 101 属于电子商品类别
# 产品 102 属于图书类别
# 产品对 (101, 103)：
# 被用户 1，3 和 4 购买（3 个消费者）
# 产品 101 属于电子商品类别
# 产品 103 属于服装类别
# 产品对 (102, 104)：
# 被用户 2，4 和 5 购买（3 个消费者）
# 产品 102 属于图书类别
# 产品 104 属于厨房用品类别
# 结果以 customer_count 降序排序。对于有相同 customer_count 的产品对，将它们以 product1_id 升序排序，然后以 product2_id 升序排序。

import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    uv = pd.merge(product_purchases, product_info, left_on='product_id', right_on='product_id', how='left')[['category', 'user_id', 'product_id']]
    print(uv)
    ans = pd.merge(uv, uv, how='cross')
    ans = ans[(ans['product_id_x'] < ans['product_id_y']) & (ans['user_id_x'] == ans['user_id_y'])]
    ans.rename(columns={'product_id_x': 'product1_id', 'product_id_y': 'product2_id', 'category_x': 'product1_category', 'category_y': 'product2_category'}, inplace=True)
    ans = (
        ans
        .groupby(['product1_id', 'product2_id', 'product1_category', 'product2_category'], dropna=False)  # 显式保留 NaN
        .agg(
            customer_count=('user_id_x', 'size')
        )
    ).reset_index()
    ans = ans[ans['customer_count'] >= 3]
    ans = ans.sort_values(by=['customer_count', 'product1_id', 'product2_id'], ascending=[False, True, True])
    return ans



data = [[1, 101, 2], [1, 102, 1], [1, 201, 3], [1, 301, 1], [2, 101, 1], [2, 102, 2], [2, 103, 1], [2, 201, 5], [3, 101, 2], [3, 103, 1], [3, 301, 4], [3, 401, 2], [4, 101, 1], [4, 201, 3], [4, 301, 1], [4, 401, 2], [5, 102, 2], [5, 103, 1], [5, 201, 2], [5, 202, 3]]
product_purchases = pd.DataFrame(data, columns=["user_id", "product_id", "quantity"])
data = [[101, 'Electronics', 100], [102, 'Books', 20], [103, 'Books', 35], [201, 'Clothing', 45], [202, 'Clothing', 60], [301, 'Sports', 75], [401, 'Kitchen', 50]]
product_info= pd.DataFrame(data, columns=["product_id", "category", "price"])

print(find_product_recommendation_pairs(product_purchases, product_info))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# with uv as(
#     select a.user_id, a.product_id, b.category from ProductPurchases a
#     left join ProductInfo b on a.product_id=b.product_id
# )
# select u1.product_id product1_id, u2.product_id product2_id, u1.category product1_category, u2.category product2_category, count(1) customer_count
# from uv u1, uv u2
#   where u1.product_id < u2.product_id and u1.user_id = u2.user_id group by u1.product_id,  u2.product_id, u1.category, u2.category having count(1)>=3
# order by customer_count desc, product1_id, product2_id;


