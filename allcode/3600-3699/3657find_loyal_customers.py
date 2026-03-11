# 表：customer_transactions
#
# +------------------+---------+
# | Column Name      | Type    |
# +------------------+---------+
# | transaction_id   | int     |
# | customer_id      | int     |
# | transaction_date | date    |
# | amount           | decimal |
# | transaction_type | varchar |
# +------------------+---------+
# transaction_id 是这张表的唯一主键。
# transaction_type 可以是 “purchase” 或 “refund”。
# 编写一个解决方案来查找 忠实客户。如果满足下述所有条件，可以认为该客户是 忠实 客户：
#
# 进行了 至少 3 次购买交易。
# 活跃了 至少 30 天。
# 他们的 退款率 少于 20%。
# 退款率是退款交易占交易总数（购买加退款）的比例，计算公式为退款交易数量除以总交易数量。
#
# 返回结果表以 customer_id 升序 排序。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# customer_transactions 表：
#
# +----------------+-------------+------------------+--------+------------------+
# | transaction_id | customer_id | transaction_date | amount | transaction_type |
# +----------------+-------------+------------------+--------+------------------+
# | 1              | 101         | 2024-01-05       | 150.00 | purchase         |
# | 2              | 101         | 2024-01-15       | 200.00 | purchase         |
# | 3              | 101         | 2024-02-10       | 180.00 | purchase         |
# | 4              | 101         | 2024-02-20       | 250.00 | purchase         |
# | 5              | 102         | 2024-01-10       | 100.00 | purchase         |
# | 6              | 102         | 2024-01-12       | 120.00 | purchase         |
# | 7              | 102         | 2024-01-15       | 80.00  | refund           |
# | 8              | 102         | 2024-01-18       | 90.00  | refund           |
# | 9              | 102         | 2024-02-15       | 130.00 | purchase         |
# | 10             | 103         | 2024-01-01       | 500.00 | purchase         |
# | 11             | 103         | 2024-01-02       | 450.00 | purchase         |
# | 12             | 103         | 2024-01-03       | 400.00 | purchase         |
# | 13             | 104         | 2024-01-01       | 200.00 | purchase         |
# | 14             | 104         | 2024-02-01       | 250.00 | purchase         |
# | 15             | 104         | 2024-02-15       | 300.00 | purchase         |
# | 16             | 104         | 2024-03-01       | 350.00 | purchase         |
# | 17             | 104         | 2024-03-10       | 280.00 | purchase         |
# | 18             | 104         | 2024-03-15       | 100.00 | refund           |
# +----------------+-------------+------------------+--------+------------------+
# 输出：
#
# +-------------+
# | customer_id |
# +-------------+
# | 101         |
# | 104         |
# +-------------+
# 解释：
#
# 客户 101:
# 购买交易：4 (IDs: 1, 2, 3, 4)
# 退款交易：0
# 退款率：0/4 = 0%（少于 20%）
# 活跃时期：1 月 5 日到 2 月 20 日 = 46 天（至少 30 天）
# 符合忠诚客户条件
# 客户 102:
# 购买交易：3 (IDs: 5, 6, 9)
# 退款交易：2 (IDs: 7, 8)
# 退款率：2/5 = 40% (超过 20%)
# 不符合忠诚客户条件
# 客户 103:
# 购买交易：3 (IDs: 10, 11, 12)
# 退款交易：0
# 退款率：0/3 = 0%（少于 20%）
# 活跃时期：1 月 1 日到 1 月 3 日 = 2 天（少于 30 天）
# 不符合忠诚客户条件
# 客户 104:
# 购买交易：5 (IDs: 13, 14, 15, 16, 17)
# 退款交易：1 (ID: 18)
# 退款率：1/6 = 16.67%（少于 20%）
# 活跃时期：1 月 1 日到 3 月 15 日 = 73 天（至少 30 天）
# 符合忠诚客户条件
# 结果表以 customer_id 升序排序。

import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    customer_transactions['purchase'] = (customer_transactions['transaction_type'].eq('purchase')).astype(int)
    ans = (
        customer_transactions
        .groupby(['customer_id'], dropna=False)   # 显式保留 NaN
        .agg(
                cnt_all=('customer_id', 'size'),
                cnt =('purchase', 'sum'),
            min_time=('transaction_date', 'min'),
            max_time=('transaction_date', 'max'),
        )
    ).reset_index()
    ans = ans[ans['cnt'] >= 3]
    ans['duration'] = (pd.to_datetime(ans['max_time']) - pd.to_datetime(ans['min_time'])) / pd.Timedelta(days=1)
    ans = ans[(ans['duration'] >= 30) & (ans['cnt'] > ans['cnt_all'] * 0.8)]

    return ans.sort_values(by=['customer_id'])[['customer_id']]


data = [[1, 101, '2024-01-05', 150.0, 'purchase'], [2, 101, '2024-01-15', 200.0, 'purchase'], [3, 101, '2024-02-10', 180.0, 'purchase'], [4, 101, '2024-02-20', 250.0, 'purchase'], [5, 102, '2024-01-10', 100.0, 'purchase'], [6, 102, '2024-01-12', 120.0, 'purchase'], [7, 102, '2024-01-15', 80.0, 'refund'], [8, 102, '2024-01-18', 90.0, 'refund'], [9, 102, '2024-02-15', 130.0, 'purchase'], [10, 103, '2024-01-01', 500.0, 'purchase'], [11, 103, '2024-01-02', 450.0, 'purchase'], [12, 103, '2024-01-03', 400.0, 'purchase'], [13, 104, '2024-01-01', 200.0, 'purchase'], [14, 104, '2024-02-01', 250.0, 'purchase'], [15, 104, '2024-02-15', 300.0, 'purchase'], [16, 104, '2024-03-01', 350.0, 'purchase'], [17, 104, '2024-03-10', 280.0, 'purchase'], [18, 104, '2024-03-15', 100.0, 'refund']]
customer_transactions = pd.DataFrame(data, columns=[
    "transaction_id",
    "customer_id",
    "transaction_date",
    "amount",
    "transaction_type"]
)


print(find_loyal_customers(customer_transactions))

# -- Write your PostgreSQL query statement below
# select customer_id from
#     (select *, case when transaction_type='purchase' then 1 else 0 end purchase from customer_transactions)
# group by customer_id
# having sum(purchase) >= 3 and  max(transaction_date) - min(transaction_date)>=30
# and sum(purchase) > count(1)*0.8
# order by customer_id;


