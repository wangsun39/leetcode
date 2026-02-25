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
# 每一行代表用户以特定数量购买的一种产品。
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
# 每一行表示一件商品的类别和价格。
# 亚马逊想要了解不同产品类别的购物模式。编写一个解决方案：
#
# 查找所有 类别对（其中 category1 < category2）
# 对于 每个类别对，确定 同时 购买了两类别产品的 不同用户 数量
# 如果至少有 3 个不同的客户购买了两个类别的产品，则类别对被视为 可报告的。
#
# 返回可报告类别对的结果表以 customer_count 降序 排序，并且为了防止排序持平，以 category1 字典序 升序 排序，然后以 category2 升序 排序。
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
# | 1       | 201        | 3        |
# | 1       | 301        | 1        |
# | 2       | 101        | 1        |
# | 2       | 102        | 2        |
# | 2       | 103        | 1        |
# | 2       | 201        | 5        |
# | 3       | 101        | 2        |
# | 3       | 103        | 1        |
# | 3       | 301        | 4        |
# | 3       | 401        | 2        |
# | 4       | 101        | 1        |
# | 4       | 201        | 3        |
# | 4       | 301        | 1        |
# | 4       | 401        | 2        |
# | 5       | 102        | 2        |
# | 5       | 103        | 1        |
# | 5       | 201        | 2        |
# | 5       | 202        | 3        |
# +---------+------------+----------+
# ProductInfo 表：
#
# +------------+-------------+-------+
# | product_id | category    | price |
# +------------+-------------+-------+
# | 101        | Electronics | 100   |
# | 102        | Books       | 20    |
# | 103        | Books       | 35    |
# | 201        | Clothing    | 45    |
# | 202        | Clothing    | 60    |
# | 301        | Sports      | 75    |
# | 401        | Kitchen     | 50    |
# +------------+-------------+-------+
# 输出：
#
# +-------------+-------------+----------------+
# | category1   | category2   | customer_count |
# +-------------+-------------+----------------+
# | Books       | Clothing    | 3              |
# | Books       | Electronics | 3              |
# | Clothing    | Electronics | 3              |
# | Electronics | Sports      | 3              |
# +-------------+-------------+----------------+
# 解释：
#
# Books-Clothing:
# 用户 1 购买来自 Books (102) 和 Clothing (201) 的商品
# 用户 2 购买来自 Books (102, 103) 和 Clothing (201) 的商品
# 用户 5 购买来自 Books (102, 103) 和 Clothing (201, 202) 的商品
# 共计：3 个用户购买同一类别的商品
# Books-Electronics:
# 用户 1 购买来自 Books (102) 和 Electronics (101) 的商品
# 用户 2 购买来自 Books (102, 103) 和 Electronics (101) 的商品
# 用户 3 购买来自 Books (103) 和 Electronics (101) 的商品
# 共计：3 个消费者购买同一类别的商品
# Clothing-Electronics:
# 用户 1 购买来自 Clothing (201) 和 Electronics (101) 的商品
# 用户 2 购买来自 Clothing (201) 和 Electronics (101) 的商品
# 用户 4 购买来自 Clothing (201) 和 Electronics (101) 的商品
# 共计：3 个消费者购买同一类别的商品
# Electronics-Sports:
# 用户 1 购买来自 Electronics (101) 和 Sports (301) 的商品
# 用户 3 购买来自 Electronics (101) 和 Sports (301) 的商品
# 用户 4 购买来自 Electronics (101) 和 Sports (301) 的商品
# 共计：3 个消费者购买同一类别的商品
# 其它类别对比如 Clothing-Sports（只有 2 个消费者：用户 1 和 4）和 Books-Kitchen（只有 1 个消费者：用户 3）共同的消费者少于 3 个，因此不包含在结果内。
# 结果按 customer_count 降序排列。由于所有对都有相同的客户数量 3，它们按 category1（然后是 category2）升序排列。

import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    uv = pd.merge(product_purchases, product_info, left_on='product_id', right_on='product_id', how='left')[['category', 'user_id']]
    uv = uv.drop_duplicates()
    print(uv)
    ans = pd.merge(uv, uv, how='cross')
    ans = ans[(ans['category_x'] < ans['category_y']) & (ans['user_id_x'] == ans['user_id_y'])]
    ans.rename(columns={'category_x': 'category1', 'category_y': 'category2'}, inplace=True)
    ans = (
        ans
        .groupby(['category1', 'category2'], dropna=False)  # 显式保留 NaN
        .agg(
            customer_count=('user_id_x', 'size')
        )
    ).reset_index()
    ans = ans[ans['customer_count'] >= 3]
    ans = ans.sort_values(by=['customer_count', 'category1', 'category2'], ascending=[False, True, True])
    return ans



data = [[1, 101, 2], [1, 102, 1], [1, 201, 3], [1, 301, 1], [2, 101, 1], [2, 102, 2], [2, 103, 1], [2, 201, 5], [3, 101, 2], [3, 103, 1], [3, 301, 4], [3, 401, 2], [4, 101, 1], [4, 201, 3], [4, 301, 1], [4, 401, 2], [5, 102, 2], [5, 103, 1], [5, 201, 2], [5, 202, 3]]
product_purchases = pd.DataFrame(data, columns=["user_id", "product_id", "quantity"])
data = [[101, 'Electronics', 100], [102, 'Books', 20], [103, 'Books', 35], [201, 'Clothing', 45], [202, 'Clothing', 60], [301, 'Sports', 75], [401, 'Kitchen', 50]]
product_info= pd.DataFrame(data, columns=["product_id", "category", "price"])

print(find_category_recommendation_pairs(product_purchases, product_info))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# with uv as(
#     select distinct category,  user_id from
#     (select user_id, category from ProductPurchases a
#     left join ProductInfo b on a.product_id=b.product_id)
# )
# select u1.category category1, u2.category category2, count(1) customer_count
# from uv u1, uv u2
#   where u1.category < u2.category and u1.user_id = u2.user_id group by u1.category,  u2.category having count(1)>=3
# order by customer_count desc, category1, category2;


