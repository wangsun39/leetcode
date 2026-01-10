# 表: Accounts
#
# +-------------+------+
# | 列名        | 类型  |
# +-------------+------+
# | account_id  | int  |
# | income      | int  |
# +-------------+------+
# 在 SQL 中，account_id 是这个表的主键。
# 每一行都包含一个银行帐户的月收入的信息。
#
#
# 查询每个工资类别的银行账户数量。 工资类别如下：
#
# "Low Salary"：所有工资 严格低于 20000 美元。
# "Average Salary"： 包含 范围内的所有工资 [$20000, $50000] 。
# "High Salary"：所有工资 严格大于 50000 美元。
#
# 结果表 必须 包含所有三个类别。 如果某个类别中没有帐户，则报告 0 。
#
# 按 任意顺序 返回结果表。
#
# 查询结果格式如下示例。
#
#
#
# 示例 1：
#
# 输入：
# Accounts 表:
# +------------+--------+
# | account_id | income |
# +------------+--------+
# | 3          | 108939 |
# | 2          | 12747  |
# | 8          | 87709  |
# | 6          | 91796  |
# +------------+--------+
# 输出：
# +----------------+----------------+
# | category       | accounts_count |
# +----------------+----------------+
# | Low Salary     | 1              |
# | Average Salary | 0              |
# | High Salary    | 3              |
# +----------------+----------------+
# 解释：
# 低薪: 有一个账户 2.
# 中等薪水: 没有.
# 高薪: 有三个账户，他们是 3, 6和 8.

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    count = [0] * 3
    for income in accounts['income']:
        if income < 20000:
            count[0] += 1
        elif income > 50000:
            count[2] += 1
        else:
            count[1] += 1

    return pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count': count})


data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})


print(count_salary_categories(accounts))

# select name as Customers from Customers  where id not in (select customerId from Orders);
# -- Write your PostgreSQL query statement below

# PostgreSQL
# select 'Low Salary' category, count(1) accounts_count from Accounts where income < 20000
# union all
# select 'Average Salary' category, count(1) accounts_count from Accounts where income between 20000 and 50000
# union all
# select 'High Salary' category, count(1) accounts_count from Accounts where income > 50000;



