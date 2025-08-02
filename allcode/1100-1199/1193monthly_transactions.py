# 表：Transactions
#
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | country       | varchar |
# | state         | enum    |
# | amount        | int     |
# | trans_date    | date    |
# +---------------+---------+
# id 是这个表的主键。
# 该表包含有关传入事务的信息。
# state 列类型为 ["approved", "declined"] 之一。
#
#
# 编写一个 sql 查询来查找每个月和每个国家/地区的事务数及其总金额、已批准的事务数及其总金额。
#
# 以 任意顺序 返回结果表。
#
# 查询结果格式如下所示。
#
#
#
# 示例 1:
#
# 输入：
# Transactions table:
# +------+---------+----------+--------+------------+
# | id   | country | state    | amount | trans_date |
# +------+---------+----------+--------+------------+
# | 121  | US      | approved | 1000   | 2018-12-18 |
# | 122  | US      | declined | 2000   | 2018-12-19 |
# | 123  | US      | approved | 2000   | 2019-01-01 |
# | 124  | DE      | approved | 2000   | 2019-01-07 |
# +------+---------+----------+--------+------------+
# 输出：
# +----------+---------+-------------+----------------+--------------------+-----------------------+
# | month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
# +----------+---------+-------------+----------------+--------------------+-----------------------+
# | 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
# | 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
# | 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
# +----------+---------+-------------+----------------+--------------------+-----------------------+


import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    print(transactions)
    transactions['ca'] = (transactions['state'] == 'approved').astype(int)
    transactions['aa'] = transactions['amount'].where(transactions['state'] == 'approved')
    ans = (
        transactions
        .groupby(['country', 'month'], dropna=False)   # 显式保留 NaN
        .agg(
                trans_count=('amount', 'size'),  # 新增：统计每组的行数
                approved_count=('ca', 'sum'),
                trans_total_amount=('amount', 'sum'),
                approved_total_amount=('aa', 'sum')
        )
    ).reset_index()
    return ans




data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})


print(monthly_transactions(transactions))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select TO_CHAR(trans_date, 'YYYY-MM') as month, country, count(1) trans_count,
# sum(case state when 'approved' then 1 else 0 end) as approved_count,
# sum(amount) as trans_total_amount,
# sum(case state when 'approved' then amount else 0 end) as approved_total_amount
# from Transactions group by country, TO_CHAR(trans_date, 'YYYY-MM');




