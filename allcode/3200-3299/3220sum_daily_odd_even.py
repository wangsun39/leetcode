# 表：transactions
#
# +------------------+------+
# | Column Name      | Type |
# +------------------+------+
# | transaction_id   | int  |
# | amount           | int  |
# | transaction_date | date |
# +------------------+------+
# transactions_id 列唯一标识了表中的每一行。
# 这张表的每一行包含交易 id，金额总和和交易日期。
# 编写一个解决方案来查找每天 奇数 交易金额和 偶数 交易金额的 总和。如果某天没有奇数或偶数交易，显示为 0。
#
# 返回结果表以 transaction_date 升序 排序。
#
# 结果格式如下所示。
#
#
#
# 示例：
#
# 输入：
#
# transactions 表：
#
# +----------------+--------+------------------+
# | transaction_id | amount | transaction_date |
# +----------------+--------+------------------+
# | 1              | 150    | 2024-07-01       |
# | 2              | 200    | 2024-07-01       |
# | 3              | 75     | 2024-07-01       |
# | 4              | 300    | 2024-07-02       |
# | 5              | 50     | 2024-07-02       |
# | 6              | 120    | 2024-07-03       |
# +----------------+--------+------------------+
#
# 输出：
#
# +------------------+---------+----------+
# | transaction_date | odd_sum | even_sum |
# +------------------+---------+----------+
# | 2024-07-01       | 75      | 350      |
# | 2024-07-02       | 0       | 350      |
# | 2024-07-03       | 0       | 120      |
# +------------------+---------+----------+
#
# 解释：
#
# 对于交易日期：
# 2024-07-01:
# 奇数交易金额总和：75
# 偶数交易金额总和：150 + 200 = 350
# 2024-07-02:
# 奇数交易金额总和：0
# 偶数交易金额总和：300 + 50 = 350
# 2024-07-03:
# 奇数交易金额总和：0
# 偶数交易金额总和：120
# 注意：输出表以 transaction_date 升序排序。

import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    ans = (
        transactions
        .groupby(['transaction_date'], dropna=False)  # 显式保留 NaN
        .agg(
            odd_sum=('amount', lambda nums: sum(x for x in nums if (x & 1) == 1)),
            even_sum=('amount', lambda nums: sum(x for x in nums if (x & 1) == 0))
        )
    ).reset_index()
    ans.sort_values(by='transaction_date', inplace=True)
    return ans




data = [[1, 150, '2024-07-01'], [2, 200, '2024-07-01'], [3, 75, '2024-07-01'], [4, 300, '2024-07-02'], [5, 50, '2024-07-02'], [6, 120, '2024-07-03']]
transactions = pd.DataFrame(data, columns=["transaction_id", "amount", "transaction_date"]).astype({"transaction_id": "int", "amount":"int", "transaction_date":"datetime64[ns]"})

print(sum_daily_odd_even(transactions))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL

# select transaction_date, sum(case when amount % 2 = 1 then amount else 0 end) odd_sum,
# sum(case when amount % 2 = 0 then amount else 0 end) even_sum from transactions group by transaction_date
# order by transaction_date;


